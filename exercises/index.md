---
layout: page
title: Exercises
---
<a href="#Python">Python</a> \| <a href="#R">R</a> \| <a href="#SQL">SQL</a>

### Python <a name="Python"></a>
<table>
  <tr>
    <th>Name</th>
    <th>Content</th>
    <th>Output</th>
  </tr>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'Python' %}
   <tr>
    <td nowrap><a href="{{ page.url | prepend: site.baseurl }}">
      {{ page.title | replace:'and','&'  }}</a></td>
    <td>{{ page.subtitle }}</td>
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    <td>
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">
          [{{ solution.path | split:"." | last}}]</a>
      {% endif %}
    {% endfor %}
    </td>
   </tr>
  {% endif %}
{% endfor %}
</table>


### R <a name="R"></a>
<table>
  <tr>
    <th>Name</th>
    <th>Content</th>
    <th>Output</th>
  </tr>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'R' %}
   <tr>
    <td nowrap><a href="{{ page.url | prepend: site.baseurl }}">
      {{ page.title | replace:'and','&'  }}</a></td>
    <td>{{ page.subtitle }}</td>
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    <td>
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">
          [{{ solution.path | split:"." | last}}]</a>
      {% endif %}
    {% endfor %}
    </td>
   </tr>
  {% endif %}
{% endfor %}
</table>

### SQL <a name="SQL"></a>
<table>
  <tr>
    <th>Name</th>
    <th>Content</th>
    <th>Output</th>
  </tr>
{% for page in site.pages %}
  {% if page.layout == 'exercise' and page.language == 'SQL' %}
   <tr>
    <td nowrap><a href="{{ page.url | prepend: site.baseurl }}">
      {{ page.title | replace:'and','&'  }}</a></td>
    <td>{{ page.subtitle }}</td>
    {% capture output_file %}{{ page.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
    <td>
    {% for solution in site.static_files %}
      {% if solution.path contains output_file %}
        <a href="{{ solution.path | prepend: site.baseurl}}">
          [{{ solution.path | split:"." | last}}]</a>
      {% endif %}
    {% endfor %}
    </td>
   </tr>
  {% endif %}
{% endfor %}
</table>