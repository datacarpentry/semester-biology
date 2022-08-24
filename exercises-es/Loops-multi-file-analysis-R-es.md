---
layout: exercise
topic: Loops
title: Multi-file Analysis
language: R
---
Tiene collares satelitales en varios individuos y desea poder ver rápidamente todos sus movimientos recientes de manera simultánea.
Los datos son publicados diariamente en [url as a zip file]({{ site.baseurl }}/data/individual_collar_data.zip) y contienen un archivo csv para cada individuo: [{{ site.url }}/data/individual_collar_data.zip]({{ site.baseurl }}/data/individual_collar_data.zip)
Comience por:

* Descargar el archivo zip usando `download.file()`
* Descomprimir el archivo usando `unzip()`
* Obtener una lista de todos los archivos que contengan en su nombre el patrón `"collar-data-.*.txt"`

1. Use un bucle (loop) para cargar cada uno de estos archivos en R y haga un diagrama de líneas (usando `geom_path()`) para cada archivo con `long` en el eje `x` y `lat` en el eje `y`.
Las gráficas, como otros tipos de salida (outputs), no se muestran dentro de el bucle (loop) a menos que se escriba explícitamente, por lo que debe colocar el comando `ggplot()` dentro de una declaración `print()`.
Incluya el nombre del archivo en la gráfica como título usando `labs()`.

2. Agregue código al bucle (loop) para calcular la latitud mínima y máxima en el archivo y almacene estos valores, junto con el nombre del archivo, en un marco de datos.
Muestra el marco de datos como salida.

Si está interesado en ver otra aplicación de bucles for (for loops), [check out the code]({{ site.baseurl }}/code/Data-simulation-for-loops-multi-file-analysis) utilizado para simular los datos de este ejercicio usando bucles for.
