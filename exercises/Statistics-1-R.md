---
layout: exercise
title: Statistics 1
subtitle: Adult Size vs. Newborn Size 2
language: R
---

This is a follow up to [Graphing 2]({{ site.baseurl }}/exercises/Graphing-2-R).

We've graphed the relationship between adult size and new born size in
mammals and now it's time to analyze the relationship statistically.

1.  Do a regression where x is log10(adult mass) and y is log10(newborn mass).
2.  Print the summary statistics for this regression.
3.  Using `ggplot` make a graph that shows both the data points and the
    regression line through those points. Either the axes or the data should be
    logarithmically scaled to match your regression analysis. You won't actually
    need to include the regression results themselves since `geom_smooth` will
    let you graph the linear model with the data. Label the axes.

*Optional: If you want, plot a histogram of the residuals of the regression to
make sure that they are roughly normally distributed (you can do this with just
a single line of code)*
