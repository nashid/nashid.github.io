---
layout: default
title: Awards
navtitle: Awards
permalink: /awards/
weight: 2
group: awards
---

### Awards and Honors

{% for award in site.data.awards %}
<div class="row service">
  <div class="left">
    {% if award.highlight %}
    <a href="{{ award.website }}" target="_blank" style="color: #d4af37; font-weight: bold;">{{ award.title }}</a>
    {% else %}
    <a href="{{ award.website }}" target="_blank">{{ award.title }}</a>
    {% endif %}
    <br/>
    <span style="font-size: 0.9em;">{{ award.description }}</span>
  </div>
  <div class="right">
    {{ award.year }}
  </div>
</div>
{% endfor %}

### Invited Talks, Visits, and Events

{% assign sorted_talks = site.data.talks | sort: "year" | reverse %}
{% for talk in sorted_talks %}
<div class="row service" style="margin-bottom: 1.2em;">
  <div class="left">
    <a href="{{ talk.website }}" target="_blank"><strong>{{ talk.title }}</strong></a>{% if talk.location %} &mdash; {{ talk.location }}{% endif %}
    <br/>
    {{ talk.description }}
  </div>
  <div class="right" style="min-width: 60px; text-align: right;">
    {{ talk.year }}
  </div>
</div>
{% endfor %}
