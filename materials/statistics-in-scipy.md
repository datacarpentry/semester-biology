---
layout: page
element: notes
title: Statistics in Scipy
language: Python
---

### Import

```python
import scipy.stats as stat
```

### Regression

```python
stat.linregress(x, y)
xs = np.array([min(x), max(x)])
p.plot(xs, reg_out[1] + xs * reg_out[0])
```

### T-tests

#### One sample against a theoretical mean

```python
t, pval = stat.ttest_1samp(x, mean)
```

#### Two samples against each other

```python
t_2samp, p_2samp = stat.ttest_ind(x, y)
```
