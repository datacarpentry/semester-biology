---
layout: page
title: Exercises
---
<a href="#Python">Python</a> | <a href="#R">R</a> | <a href="#SQL">SQL</a>

### Python <a name="Python"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'Python' %}
    <li>
    <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
    {{ page.subtitle | prepend: "<-- " | append: " -->" }}
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">output</a>
      {% endif %}
    {% endfor %}
    </li>
  {% endif %}
{% endfor %}
</ul>

### R <a name="R"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'R' %}
    <li>
    <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
    {{ page.subtitle | prepend: "<-- " | append: " -->" }}
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">output</a>
      {% endif %}
    {% endfor %}
    </li>
  {% endif %}
{% endfor %}
</ul>

### SQL <a name="SQL"></a>
<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'SQL' %}
    <li>
    <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
    {{ page.subtitle | prepend: "<-- " | append: " -->" }}
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">output</a>
      {% endif %}
    {% endfor %}
    </li>
  {% endif %}
{% endfor %}
</ul>