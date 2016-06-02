---
layout: page
title: Exercises
languages: ['Access', 'Python', 'R', 'SQL']
---
<a href="#Access">Access</a> \| <a href="#Python">Python</a> \| <a href="#R">R</a> \| <a href="#SQL">SQL</a>

{% for language in page.languages %}
  <h3> {{ language }} <a name="{{ language }}"></a></h3>
  <table>
    <tr>
      <th>Topic</th>
      <th>Title</th>
      <th>Output</th>
    </tr>
  {% for exercise in site.pages %}
    {% if exercise.layout == 'exercise' and exercise.language == language %}
     <tr>
      <td nowrap>{{ exercise.topic | replace:'and','&'  }}</td>
      <td nowrap><a href="{{ exercise.url | prepend: site.baseurl }}">
        {{ exercise.title }}</a></td>
      {% capture output_file %}{{ exercise.url | remove: 'exercises' | remove: '/' | prepend: '/solutions/' }}{% endcapture %}
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
  <p align="right"><font size="-1">
    <a href="{{ site.baseurl }}/exercises/">[back to top]</a>
  </font></p>
{% endfor %}