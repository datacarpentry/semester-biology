---
layout: exercise
topic: Capstone
title: Cocili Data Exploration
language: R
---

Understanding the spatial distribution of ecological phenomena is central to the
study of natural systems. A group of scientists has collected a dataset on the
size, location, and species identify of all of the trees in a 4 ha site in
Panama call "Cocoli".

Download the [Cocoli Data](http://ctfs.si.edu/webatlas/datasets/cocoli/cocoli.zip)
and explore the following spatial properties.

1. Make a single plot showing the location of each tree for all species with
   more than 100 individuals. Each species should be in its own subplot (i.e.,
   facet). Label the subplots with the genus and species names, not the species
   code. Scale the size of the point by its stem diameter (use `dbh1`) so that
   larger trees display as larger points. Have the code save the plot in a
   `figures` folder in your project.
2. [Basal area](https://en.wikipedia.org/wiki/Basal_area) is a common measure in
   forest management and ecology. It is the sum of the cross-sectional areas of
   all of the trees occuring in some area and can be calculated as the sum of
   0.00007854 * DBH^2 over all of the trees. To look at how basal area varies
   across the site divide the site into 100 m^2 sample regions (10 x 10 m cells)
   and determining the total basal area in each region. I.e., take all of the
   trees in a grid cell where x is between 0 and 10 and y is between 0 and 10
   and determine their basal area. Do the same thing for x between 0 and 10 and
   y between 10 and 20, and so on. You can do this using two "nested" for loops
   to subset the data and calculate the basal area in that region. Make a plot
   that shows how the basal area varies spatially. Since the calculation is for
   a square region, plot it that way using `geom_tile()` with the center of the
   tile at the center of the region where basal area was calculated. Have the
   code save the plot in a `figures` folder in your project.


Comprender la distribución espacial de los fenómenos ecológicos es fundamental para la
estudio de los sistemas naturales. Un grupo de científicos ha recopilado datos sobre el tamaño, ubicación e identificación de especies de todos los árboles en un sitio de 4 hectareas en "Cocoli",
Panamá.

Descargue los [Datos de Cocoli] [Cocoli Data](http://ctfs.si.edu/webatlas/datasets/cocoli/cocoli.zip)
and explore the following spatial properties.

1. Haga una sola gráfica que muestre la ubicación de cada árbol para todas las especies con
   más de 100 individuos. Cada especie debe estar en su propia subgráfica (subplot) (es decir,
   faceta). Etiquete las subgráfica (subplots) con los nombres de género y especie, no la especie
   código. El tamaño del punto debe ser determinado por el diámetro de tallo (use `dbh1`) para que
   los árboles más grandes se muestran como puntos más grandes. Haga que el código guarde las gráficas en un carpeta `figures` en su proyecto.

2. [Basal area](https://en.wikipedia.org/wiki/Basal_area) es una medida común en el
   manejo y conservación de bosques y ecología. Es la suma de las áreas de las secciones 	    
   transversales (cross-sectional areas) de
   todos los árboles que se encuentran en un área y se puede calcular como la suma de
   0.00007854 * DAP^2 sobre todos los árboles. Para ver cómo varía el área basal
   en todo el sitio, divida el sitio en regiones de muestra de 100 m^2 (celdas de 10 x 10 m)
   y determine el área basal total en cada región. Es decir, tome todos los
   árboles en una celda de cuadrícula donde X está entre: 0 y 10 e Y: entre 0 y 10
   y determine su área basal. Haga lo mismo para X entre: 0 y 10 y para
   Y: entre 10 y 20, y así sucesivamente. Puede hacer esto usando dos bucles for (for loops) "anidados"
   para crear un subconjunto de los datos y calcular el área basal en esa región. Haga una gráfica
   que muestre cómo el área basal varía espacialmente. Como el cálculo es para
   una región cuadrada, trácela de esa manera usando `geom_tile()` con el centro de la
   mosaico en el centro de la región donde se calculó el área basal. Guarde la gráfica en una carpeta `figures` en su proyecto.