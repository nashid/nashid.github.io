---
layout: default
title: Writings
navtitle: Writings
permalink: /writings/
weight: 8
group: writings
---

The biggest barriers in academia are often not ability but *access*, including access to the tacit knowledge that nobody writes down. These writings are my attempt to write it down: the processes, norms, and decisions that shape a research career but rarely appear in any handbook. Doing so in public is part of my broader commitment to [broadening access to research training](/mentorship/).

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
