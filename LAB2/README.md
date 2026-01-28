# Lab 2: Data Cleaning and Exploratory Data Analysis on Diabetes Dataset

## Overview
This lab focuses on **data cleaning, preprocessing, and exploratory data analysis (EDA)**
using the **Diabetes dataset**. The objective is to prepare raw data for machine learning
by identifying inconsistencies, handling outliers, analyzing feature relationships,
and applying feature scaling techniques.

The experiment is implemented using **Python**, **pandas**, **scikit-learn**,
**matplotlib**, and **seaborn**, with all intermediate and final outputs saved
as image files.

---

## Objectives
- To inspect and understand the structure of the dataset
- To perform statistical analysis on numerical features
- To detect and remove outliers using visualization and IQR method
- To analyze correlations between features and the target variable
- To visualize class distribution of the target variable
- To apply normalization and standardization techniques

---

## Dataset
- **Dataset Name:** Diabetes Dataset
- **File Used:** `diabetes.csv`
- **Number of Records:** 768
- **Number of Features:** 8 + 1 target
- **Features:**
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
- **Target Variable:**
  - **Outcome**
    - 0 → No Diabetes
    - 1 → Diabetes

---

## Tools and Libraries Used
- Python 3
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

## Exploratory Data Analysis (EDA)

The following visualizations were generated to understand data distribution,
outliers, feature relationships, and target balance:

| Image File Name            | Description                                     |
| -------------------------- | ----------------------------------------------- |
| `boxplots.png`             | Boxplots for detecting outliers in all features |
| `correlation_heatmap.png`  | Correlation matrix heatmap of all variables     |
| `outcome_distribution.png` | Pie chart showing diabetes outcome distribution |

---

## Data Cleaning and Preprocessing Steps

### 1. Data Inspection
- Loaded dataset using pandas
- Checked data types and structure using `df.info()`
- Verified missing values using `df.isnull().sum()`

---

### 2. Statistical Summary
- Generated descriptive statistics using `df.describe()`
- Analyzed mean, median, standard deviation, and quartiles

---

### 3. Outlier Detection
- Used boxplots to visualize feature-wise data spread
- Identified extreme values in features such as:
  - Insulin
  - SkinThickness
  - BMI
  - Age

**Output Image:**
- `boxplots.png`

---

### 4. Outlier Removal
- Applied **Interquartile Range (IQR)** method
- Removed values outside the acceptable range
- Improved overall data quality and consistency

---

### 5. Correlation Analysis
- Computed correlation matrix using `df.corr()`
- Visualized correlations using a heatmap
- Observed that **Glucose** has the strongest correlation with the target variable

**Output Image:**
- `correlation_heatmap.png`

---

### 6. Target Variable Distribution
- Visualized class balance using a pie chart
- Dataset distribution:
  - 65% → No Diabetes
  - 35% → Diabetes

**Output Image:**
- `outcome_distribution.png`

---

### 7. Feature and Target Separation
- Features (`X`) extracted by removing the `Outcome` column
- Target (`y`) set as the `Outcome` column

---

### 8. Feature Scaling
**Normalization (Min-Max Scaling):**
- Scaled features to a range between 0 and 1
- Suitable for distance-based algorithms
**Standardization (StandardScaler):**
- Transformed features to have mean = 0 and standard deviation = 1
- Suitable for normally distributed data

---

## Output Visualizations Summary

All generated plots are saved and included in the repository for evaluation.

| Image File Name            | Purpose                       |
| -------------------------- | ----------------------------- |
| `boxplots.png`             | Outlier detection             |
| `correlation_heatmap.png`  | Feature relationship analysis |
| `outcome_distribution.png` | Target class distribution     |

---

## Files Included

| File Name             | Description                             |
| --------------------- | --------------------------------------- |
| `diabetes.csv`        | Dataset used for the experiment         |
| `data_cleaning.ipynb` | Complete data cleaning and EDA notebook |
| `DATA CLEANING.pdf`   | Theory and step-by-step explanation     |
| `README.md`           | Documentation for Lab 2                 |
| `*.png`               | Saved output visualizations             |

---

## Results
- Dataset was successfully cleaned and preprocessed
- Outliers were identified and handled effectively
- Glucose was found to be the most influential feature
- Feature scaling prepared data for machine learning models

---

## Conclusion
This lab demonstrates a complete data preprocessing pipeline, including
inspection, cleaning, visualization, correlation analysis, and feature scaling.
The resulting dataset is well-structured and ready for machine learning
classification tasks.

---

## How to Run
1. Ensure `diabetes.csv` is present in the working directory
2. Open `data_cleaning.ipynb` in Jupyter Notebook or VS Code
3. Run all cells sequentially (top to bottom)
4. View generated plots and saved output images

---

## Author
**Kamalesh S P**<br>
Full Stack Developer<br>
Rajalakshmi Engineering College<br>
