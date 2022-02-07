---
layout: exercise
topic: Knitr
title: Reproducible Breeding Bird Survey Analysis
language: R
translation: es
titulo: Un estudio de reproducción de aves reproducible
---
Está interesado en comprender cómo varía la biodiversidad de las aves en
respuesta a las variables ambientales. Quiere que su análisis sea reproducible, así que usa `knitr` y` rmarkdown`. Específicamente quiere saber cómo species richness (abundancia de especies: el número de especies vistas en un sitio) varía en respuesta a la temperatura media anual y la precipitación media anual.

1. Inicie un nuevo documento "Rmd", asigne un título, asigne un autor y establezca el formato de salida como `html_document`.
2. Agregue un markdown chunk (trozo de código) que describa la pregunta que va a hacer.
3. Agregue un markdown chunk (trozo de código) que cargue los paquetes necesarios. Oculte el texto de cuando los paquetes se cargan usando `message = FALSE`.
4. Agregue un header (encabezado) relacionado a la descarga e importación de datos.
5. Agregue una sección de texto que describa brevemente los dos conjuntos de datos que va a utilizar.
6. Agregue un markdown chunk (trozo de código) para descargar los datos de Breeding Bird Surveys usando el Paquete `rdataretriever`. Instrucciones para instalar este paquete y el
   paquete de Python asociado están disponibles en el
   [Data Retriever] (https://www.data-retriever.org/). Tomará un
   mucho tiempo para descargar y convertir estos datos en un conjunto de archivos CSV utilizables
   (~ 30 minutos), así que agregue una declaración condicional que verifique si los archivos necesarios ya han sido creados y solo instale los datos si
   no existen. No muestre la salida de este markdown chunk.
7. Agregue un markdown chunk (trozo de código) para cargar las tablas de especies, recuentos y rutas en R y muestre las primeras filas de cada tabla.
8.Haga un mapa de las ubicaciones de todas las rutas de Breeding Bird Surveys,
   incluyendo el contorno de la masa continental de América del Norte. Agrega un encabezado (header) sobre este mapa describiendo lo que muestra. Puede obtener un mapa del mundo usando
   `usmap = map_data (" world ")`, que luego puede trazar usando `geom_polygon`.
   Para mostrar solo estos datos en la región de las rutas de la Breeding Bird Surveys, agregue
   lo siguiente para su comando `ggplot`:

   ```
   scale_x_continuous(limits = c(min(routes$longitude), max(routes$longitude))) +
   scale_y_continuous(limits = c(min(routes$latitude), max(routes$latitude)))
   ```

9. Utilice la función `getData` del paquete `raster` para obtener los datos de bioclim (`getData ('worldclim', var = 'bio', res = 10)`) y `extraer` los valores
   para cada ruta. Convierta la matriz resultante en un marco de datos y `select` solo
   la temperatura media anual (bio1) y la precipitación media anual (bio1).
   Utilice `cbind` para combinar estas dos columnas de variables predictoras con la tabla de rutas.
10. Determine la riqueza de especies en cada ruta del año 2015. Para obtener rutas únicas
   necesitará agrupar por las columnas `statenum` y` route`. Una estos datos con los datos que obtuvo en (7). Visualice los datos de la nueva tabla.
11.Haga dos gráficas, que muestren la relación entre `bio1` y
   `riqueza` ,` bio12` y `riqueza`. Incluya los puntos de datos no procesados y una
   línea suave a través de ellos. (* opcional *) Intente hacer esto con una función si
   quiero un desafío extra.
12. Escriba una breve sección de conclusiones que proporcione su interpretación de los
    resultados.
13. Regrese a la sección de datos de su documento y agregue citas para ambos
    conjuntos de datos. Deberá crear un archivo `.bib` para contener su bibtex
    citas. Puede obtener bibtex para las citas buscando en Google
    Scholar de "Breeding Bird Survey" y "Worldclim", haciendo clic en el botón `"`
    y seleccionando `bibtex`. También debe agregar un header (encabezado) `References` en
    la parte inferior de su documento ya que las referencias aparecerán al final.