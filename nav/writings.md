---
layout: default
title: Writings
navtitle: Writings
permalink: /writings/
weight: 8
group: writings
---

Occasional long-form writing about the tacit side of research — the processes, norms, and decisions that shape an academic career but rarely get written down. These pieces exist because I found myself explaining the same things over and over; making them public is part of my broader goal of [broadening access to research training](/mentorship/).

<ul class="post-list">
{% assign sorted_writings = site.writings | sort: "date" | reverse %}
{% for writing in sorted_writings %}
  <li>
    <span class="post-meta">{{ writing.date | date: "%B %-d, %Y" }}</span>
    <h2>
      <a class="post-link" href="{{ writing.url | prepend: site.baseurl }}">{{ writing.title }}</a>
    </h2>
    {% if writing.summary %}<p>{{ writing.summary }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
