---
layout: page
title: Exercises
languages: ['SQL', 'R', 'Python', 'Access']
---
<a href="#SQL">SQL</a> \| <a href="#R">R</a> \| <a href="#Python">Python</a> \|  <a href="#Access">Access</a>

{% for language in page.languages %}
  <h3> {{ language }} <a name="{{ language }}"></a></h3>

  {% if language == 'Python' or language == 'Access' %}
  <i>{{ language }} exercises were used in 
  <a href="http://www.programmingforbiologists.org/">previous iterations</a>
  of the course at Utah State University, but are no longer under active 
  development.</i>
  {%endif%}

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