---
layout: page
title: Exercises
---
<a href="#Python">Python</a> | <a href="#R">R</a> | <a href="#SQL">SQL</a>

### Python <a name="Python"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'Python' %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### R <a name="R"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'R' %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### SQL <a name="SQL"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'SQL' %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>