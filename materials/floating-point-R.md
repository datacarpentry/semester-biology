---
layout: page
element: notes
title: Floating Point
language: R
---

> * Did you notice anything weird while finishing the Choice Operations exercise?
> * Take a closer look at item 4.

### Floating point

```r
> x <- 1.3
> y <- 2.8
>  x * 2 + 0.2 == y
[1] FALSE
> 1.3 * 2 + 0.2
[1] 2.8
```

* What's going on?
* Unexpected result from computer arithmetic
* Numbers combine to include very small trailing digit  
* See this more easily in Python

```r
>>> 1.3 * 2 + 0.2 == 2.8
False
>>> 1.3 * 2 + 0.2
2.8000000000000003
```

## Testing equality with decimals

* `round(x * 2 + 0.2, 1) == y`
* `all.equal(x * 2 + 0.2, y)`
