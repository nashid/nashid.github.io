---
layout: default
title: Papers
permalink: /papers/
weight: 3
group: pubs
---

{% assign papers_by_year = site.data.papers | group_by_exp:"paper", "paper.year | plus: 0" %}
{% for year in papers_by_year %}
  <h3>{{ year.name }}</h3>
  {% for paper in year.items %}
  <div class="publication" id="{{ paper.id }}">
    <div class="publication-title">
      {{ paper.authors | replace: "Noor Nashid", "<b>Noor Nashid</b>" | replace: "Namavar Marjane", "<b>Namavar Marjane</b>" | replace: "(Both authors contributed equally)", "<i><b>(Both authors contributed equally)</b></i>" }}. {{ paper.title }}. {{ paper.venue }}{% if paper.pages %}, {{ paper.pages }}{% endif %}.
      {% if paper.award %}
      <br/><span class="icon" style="margin-top: 3px; display: inline-block;">
        <svg><use xlink:href="#icon-award"/></svg>
        <b>{{ paper.award }}</b>
      </span>
      {% endif %}
    </div>
    <div class="right">
      {% if paper.arxiv %}
      <a href="{{ paper.arxiv }}" target="_blank">
        <span class="icon"><svg><use xlink:href="#icon-pdf"/></svg></span>
      </a>
      {% elsif paper.doi %}
      <a href="{{ paper.doi }}" target="_blank">
        <span class="icon"><svg><use xlink:href="#icon-pdf"/></svg></span>
      </a>
      {% else %}
      <a href="{{ "/resources/papers/" | append: paper.id | append: ".pdf" | prepend: site.baseurl }}" target="_blank">
        <span class="icon"><svg><use xlink:href="#icon-pdf"/></svg></span>
      </a>
      {% endif %}
      {% if paper.code %}
      <a href="{{ paper.code }}" target="_blank">
        <span class="icon"><svg><use xlink:href="#icon-github"/></svg></span>
      </a>
      {% endif %}

      {% if paper.video %}
      <a href="{{ paper.video }}" target="_blank">
        <span class="icon"><svg><use xlink:href="#icon-youtube"/></svg></span>
      </a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
{% endfor %}
