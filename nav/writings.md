---
layout: default
title: Writings
navtitle: Writings
permalink: /writings/
weight: 8
group: writings
---

<div class="post" markdown="1">
The biggest barriers in academia are often not ability but *access*, including access to the tacit knowledge that nobody writes down. These writings are my attempt to write it down: the processes, norms, and decisions that shape a research career but rarely appear in any handbook. Doing so in public is part of my broader commitment to [broadening access to research training](/mentorship/).

<ul class="post-list">
{% assign sorted_writings = site.writings | sort: "date" | reverse %}
{% for writing in sorted_writings %}
  <li>
    <p class="post-meta"><span>{{ writing.date | date: "%B %-d, %Y" }}</span><span class="kicker-dot"></span><span>{% assign words = writing.content | strip_html | number_of_words %}{{ words | plus: 199 | divided_by: 200 }} min read</span></p>
    <h2>
      <a class="post-link" href="{{ writing.url | prepend: site.baseurl }}">{{ writing.title }}</a>
    </h2>
    {% if writing.summary %}<p class="post-excerpt">{{ writing.summary }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
</div>
