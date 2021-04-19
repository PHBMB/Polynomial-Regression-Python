# Polynomial-Regression-Python

## Overfitting vs. Underfitting
The problem of Overfitting vs Underfitting finally appears when we talk about the polynomial degree. The degree represents how much flexibility is in the model, with a higher power allowing the model freedom to hit as many data points as possible. An underfit model will be less flexible and cannot account for the data. The best way to understand the issue is to take a look at models demonstrating both situations.

#### Graph Order: 1 and R2 Score:  0.17379832589037147
![]( https://github.com/PHBMB/Polynomial-Regression-Python/blob/main/GraphOrder1.png)

#### Graph Order: 3 and R2 Score:  0.9226386619999667
![](https://github.com/PHBMB/Polynomial-Regression-Python/blob/main/GraphOrder3.png)
#### Graph Order: 15 and R2 Score:  0.9986481085821025
![](https://github.com/PHBMB/Polynomial-Regression-Python/blob/main/GraphOrder15.png)

### Conclusions
Since the data is never perfect, the goal should not be a function that intersects every point perfectly. The goal should be a function that correlates smartly with all data points. Only in this way does a prediction with data appear to be approximate.
