---
layout: page
title: Exercises
---

<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
