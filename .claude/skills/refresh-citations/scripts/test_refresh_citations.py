#!/usr/bin/env python3
"""Tests of refresh_citations.py. They use saved pages and need no network.

Run from the repository root:
    python3 -m unittest discover -s .claude/skills/refresh-citations/scripts -p "test_*.py"
"""

import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "refresh_citations.py")
PAPER = "Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning"

SENTENCE = "over {} citations (h-index: {}), including CEDAR which has been cited more than {} times"
PAGE = (
    "---\r\nlayout: default\r\n---\r\n\r\n"
    "My work has been recognized. My research has received {} and featured in an article.\r\n\r\n"
    "A second paragraph.\r\n"
)


def profile(total, h_index, paper, title=PAPER):
    """Return a page with the markup of a Google Scholar profile."""
    row = '<tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="t">{}</a></td><td class="gsc_rsb_std">{}</td><td class="gsc_rsb_std">{}</td></tr>'
    paper_row = '<tr class="gsc_a_tr"><td class="gsc_a_t"><a href="/citations?x" class="gsc_a_at">{}</a></td><td class="gsc_a_c"><a href="https://scholar.google.com/x" class="gsc_a_ac gs_ibl">{}</a></td></tr>'
    return (
        '<html><body><div id="gsc_prf_in">Noor Nashid</div><table id="gsc_rsb_st"><tbody>'
        + row.format("Citations", total, 600)
        + row.format("h-index", h_index, 11)
        + row.format("i10-index", 14, 13)
        + "</tbody></table><table>"
        + paper_row.format("Communication system", 52)
        + paper_row.format(title + ". In 2023 IEEE/ACM 45th International Conference", paper)
        + "</table></body></html>"
    )


class RefreshCitations(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.page = os.path.join(self.directory.name, "index.md")
        self.source = os.path.join(self.directory.name, "profile.html")

    def tearDown(self):
        self.directory.cleanup()

    def run_script(self, numbers, source, write=False, sentence=SENTENCE):
        with open(self.page, "wb") as handle:
            handle.write(PAGE.format(sentence.format(*numbers)).encode("utf-8"))
        with open(self.source, "w", encoding="utf-8") as handle:
            handle.write(source)
        command = [sys.executable, SCRIPT, "--page", self.page, "--profile", self.source]
        done = subprocess.run(command + (["--write"] if write else []), capture_output=True, text=True)
        with open(self.page, "rb") as handle:
            return done.returncode, done.stdout + done.stderr, handle.read()

    def original(self, numbers, sentence=SENTENCE):
        return PAGE.format(sentence.format(*numbers)).encode("utf-8")

    def test_current_sentence(self):
        code, _, page = self.run_script((700, 13, 350), profile(736, 13, 366), write=True)
        self.assertEqual(code, 0)
        self.assertEqual(page, self.original((700, 13, 350)))

    def test_report_makes_no_edit(self):
        code, output, page = self.run_script((700, 12, 350), profile(736, 13, 366))
        self.assertEqual(code, 1)
        self.assertIn('"h-index: 12" becomes "h-index: 13"', output)
        self.assertEqual(page, self.original((700, 12, 350)))

    def test_write_changes_the_numbers_only(self):
        code, _, page = self.run_script((700, 12, 350), profile(1012, 14, 451), write=True)
        self.assertEqual(code, 1)
        self.assertEqual(page, self.original((1000, 14, 450)))
        self.assertEqual(page.count(b"\r\n"), self.original((700, 12, 350)).count(b"\r\n"))

    def test_a_count_with_a_comma(self):
        code, _, page = self.run_script((700, 12, 350), profile("1,012", 14, "1,451"), write=True)
        self.assertEqual(code, 1)
        self.assertEqual(page, self.original((1000, 14, 1450)))

    def test_an_exact_multiple_is_not_over_itself(self):
        # 700 citations are not "over 700", and 350 are not "more than 350".
        code, _, page = self.run_script((600, 13, 300), profile(700, 13, 350), write=True)
        self.assertEqual(code, 1)
        self.assertEqual(page, self.original((650, 13, 300)))

    def test_one_above_a_multiple(self):
        code, _, page = self.run_script((600, 13, 300), profile(701, 13, 351), write=True)
        self.assertEqual(code, 1)
        self.assertEqual(page, self.original((700, 13, 350)))

    def test_a_lower_source_is_an_error(self):
        code, output, page = self.run_script((700, 12, 350), profile(640, 13, 366), write=True)
        self.assertEqual(code, 2)
        self.assertIn("lower number", output)
        self.assertEqual(page, self.original((700, 12, 350)))

    def test_a_lower_h_index_is_an_error(self):
        code, _, page = self.run_script((700, 13, 350), profile(736, 12, 366), write=True)
        self.assertEqual(code, 2)
        self.assertEqual(page, self.original((700, 13, 350)))

    def test_pages_that_are_not_the_profile(self):
        pages = {
            "captcha": "<html>Our systems have detected unusual traffic. Please show you are not a robot.</html>",
            "consent": '<html><form action="https://consent.google.com/save">Before you continue</form></html>',
            "sign in": '<html><a href="https://accounts.google.com/ServiceLogin">Sign in</a></html>',
        }
        for name, source in pages.items():
            with self.subTest(page=name):
                code, _, page = self.run_script((700, 12, 350), source, write=True)
                self.assertEqual(code, 3)
                self.assertEqual(page, self.original((700, 12, 350)))

    def test_a_changed_layout(self):
        code, _, page = self.run_script((700, 12, 350), "<html><body>A page without statistics</body></html>", write=True)
        self.assertEqual(code, 2)
        self.assertEqual(page, self.original((700, 12, 350)))

    def test_a_missing_row_does_not_shift_the_values(self):
        # Without the row of citations, the h-index must not be read as the total.
        source = profile(736, 13, 366).replace(">Citations</a>", ">Cited by</a>")
        code, _, page = self.run_script((700, 12, 350), source, write=True)
        self.assertEqual(code, 2)
        self.assertEqual(page, self.original((700, 12, 350)))

    def test_the_paper_is_missing(self):
        code, _, page = self.run_script((700, 12, 350), profile(736, 13, 366, title="Another paper"), write=True)
        self.assertEqual(code, 2)
        self.assertEqual(page, self.original((700, 12, 350)))

    def test_the_sentence_was_reworded(self):
        reworded = "more than {} citations (h-index: {}), with CEDAR cited {} times"
        code, _, page = self.run_script((700, 12, 350), profile(736, 13, 366), write=True, sentence=reworded)
        self.assertEqual(code, 2)
        self.assertEqual(page, self.original((700, 12, 350), sentence=reworded))


if __name__ == "__main__":
    unittest.main()
