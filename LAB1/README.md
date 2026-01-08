# Lab 1: Univariate, Bivariate and Multivariate Regression using Iris Dataset

## Overview
This lab implements **Univariate, Bivariate, and Multivariate Linear Regression**
on the **Iris dataset** to analyze relationships between flower features.
In addition to regression models, exploratory data visualizations are generated
to understand feature distributions and correlations.

The experiment is implemented using **Python**, **pandas**, **scikit-learn**,
**matplotlib**, and **seaborn**, with all outputs saved as image files.

---

## Objectives
- To explore the Iris dataset using visualization techniques
- To implement univariate, bivariate, and multivariate regression models
- To analyze relationships between independent and dependent variables
- To visualize and interpret regression results
- To evaluate model performance using R-squared values

---

## Dataset
- **Dataset Name:** Iris Dataset
- **File Used:** `iris.csv`
- **Features:**
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target Variable:**
  - Sepal Length (cm)
- **Class Labels:**
  - Setosa
  - Versicolor
  - Virginica

---

## Tools and Libraries Used
- Python 3
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- mpl_toolkits.mplot3d

---

## Exploratory Data Analysis (EDA)

The following plots were generated to understand feature distributions
and inter-feature relationships:

| Image File Name | Description |
|-----------------|-------------|
| `sepal_length_distribution.png` | Distribution of Sepal Length across species |
| `sepal_width_distribution.png` | Distribution of Sepal Width across species |
| `sepal_width_vs_petal_width.png` | Relationship between Sepal Width and Petal Width |
| `pairplot_iris.png` | Pairwise relationships among all features |

---

## Regression Experiments

### 1. Univariate Regression
- **Independent Variable:** Petal Length (cm)
- **Dependent Variable:** Sepal Length (cm)
- A linear regression model is trained using a single feature.
- The regression line and actual data points are visualized.

**Output Image:**
- `univariate_regression.png`

---

### 2. Bivariate Regression
- **Independent Variables:**
  - Petal Length (cm)
  - Petal Width (cm)
- **Dependent Variable:** Sepal Length (cm)
- A bivariate linear regression model is trained.
- Results are visualized using a **3D scatter plot**.

**Output Image:**
- `bivariate_regression.png`

---

### 3. Multivariate Regression
- **Independent Variables:** All feature variables
- **Dependent Variable:** Sepal Length (cm)
- A multivariate linear regression model is trained.
- Actual values are compared with predicted values.

**Output Image:**
- `multivariate_regression.png`

---

## Output Visualizations Summary

All generated plots are saved and included in the repository for evaluation.

| Image File Name | Purpose |
|-----------------|---------|
| `sepal_length_distribution.png` | Feature distribution analysis |
| `sepal_width_distribution.png` | Feature distribution analysis |
| `sepal_width_vs_petal_width.png` | Feature relationship analysis |
| `pairplot_iris.png` | Multivariate feature relationships |
| `univariate_regression.png` | Univariate regression output |
| `bivariate_regression.png` | Bivariate regression (3D) output |
| `multivariate_regression.png` | Multivariate regression output |

---

## Files Included

| File Name | Description |
|----------|-------------|
| `iris.csv` | Dataset used for the experiment |
| `Lab 1a.ipynb` | EDA, univariate and bivariate regression |
| `Lab 1b.ipynb` | Multivariate regression and evaluation |
| `README.md` | Documentation for Lab 1 |
| `*.png` | Saved output plots |

---

## Results
- Exploratory plots reveal clear feature separability among species.
- Regression models were implemented successfully.
- Saved plots provide clear visual interpretation of model behavior.
- R-squared values indicate strong predictive performance.

---

## Conclusion
This lab demonstrates the effective use of exploratory data analysis
and regression techniques on the Iris dataset. Visualizations combined
with regression modeling provide valuable insights into feature
relationships and predictive behavior.

---

## How to Run
1. Ensure `iris.csv` is present in the working directory
2. Open `Lab 1a.ipynb` and `Lab 1b.ipynb` in Jupyter Notebook or VS Code
3. Run all cells sequentially (top to bottom)
4. View generated plots and saved output images

---

## Author
**Kamalesh S P**\
Full Stack Developer\
Rajalakshmi Engineering College\
