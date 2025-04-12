# 📊 Suicide Rates Exploratory Data Analysis (EDA)

This project presents an in-depth Exploratory Data Analysis (EDA) of a global suicide rates dataset. The goal is to uncover patterns, trends, and disparities across different demographics such as sex, age group, and race, as well as to observe changes over time.

---

## 🔍 Project Overview

Understanding suicide trends is critical for shaping public health policies and targeted mental health interventions. Through data analysis and visualization, this project aims to provide valuable insights into the societal and demographic factors contributing to suicide rates.

---

## 📁 Dataset Description

The dataset includes variables such as:
- **Year**
- **Country**
- **Sex**
- **Age Group**
- **Race** (if available)
- **Number of Suicides**
- **Population**
- **Suicide Rate (calculated)**

---

## 🧠 Analysis Performed

Each analysis follows a structured approach:

### 1. Suicide Rates by Sex
- **Introduction**: Assess gender-based disparities.
- **Description**: Grouped data by sex.
- **Methods**: `groupby()`, `mean()`.
- **Findings**: Males have significantly higher suicide rates.
- **Visualization**: Bar plot.

### 2. Suicide Rates by Age Group
- **Introduction**: Determine which age groups are most vulnerable.
- **Description**: Analyzed suicide rates across age ranges.
- **Methods**: Aggregation and averaging.
- **Findings**: Highest rates observed in 65+ group.
- **Visualization**: Bar plot.

### 3. Suicide Rates by Race
- **Introduction**: Explore race-based disparities.
- **Description**: Race-wise segmentation (if data available).
- **Methods**: `groupby()`, percentage calculations.
- **Findings**: Distinct differences found across races.
- **Visualization**: Stacked bar/heatmap.

### 4. Trend Analysis Over Time
- **Introduction**: Study historical suicide patterns.
- **Description**: Year-wise aggregation.
- **Methods**: Time series grouping.
- **Findings**: Increasing trends observed post-2000.
- **Visualization**: Line plot.

---

## 📈 Visualizations

Created using:
- **Seaborn**: For comparative visualizations
- **Matplotlib**: For customized plots
- **Heatmaps & Line Charts**: To observe temporal and categorical patterns

---

## 🔮 Future Scope

- Advanced demographic and regional analysis
- Predictive modeling for suicide trends using ML
- Longitudinal studies on mental health policies
- Impact evaluation of global intervention programs

---

## 📚 References

- [World Health Organization (WHO)](https://www.who.int/mental_health/suicide-prevention/world_report_2014/en/)
- Nock et al., *Suicide and Suicidal Behavior* (Epidemiologic Reviews, 2008)
- Klonsky & May, *Three-Step Theory of Suicide* (2015)
- National Library of Medicine: [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov)

---

## 📌 Conclusion

This analysis highlights the importance of data-driven approaches to understanding complex social issues like suicide. The insights gained can guide future research, inform public policy, and support mental health advocacy.

---

## 🤝 Contributions

Feel free to fork this repository, submit issues, or open pull requests if you'd like to build on this work!

---

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).

