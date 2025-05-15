# COVID-19 Global Data Analysis Report

**Data Source:** [Our World in Data - COVID-19 Dataset](https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv)  
**Tools Used:** `pandas`, `matplotlib`, `seaborn`, `plotly`  
**Time Frame:** 2019–Current

---

## Objectives

- Import and clean COVID-19 global data.
- Analyze trends in total cases, deaths, and vaccinations over time.
- Compare daily new cases between selected countries.
- Calculate and compare death rates by country.
- Analyze and visualize global vaccination rollouts.
- Present findings using clear visualizations and summaries.

---

## 1. Data Preparation

- Dataset imported using Pandas.
- Cleaned by removing global/aggregate entries and handling missing values.
- Converted `date` column to datetime format for time series analysis.

---

## 2. Total Cases, Deaths, and Vaccinations Over Time

- **Line charts** plotted for:
  - Total confirmed cases
  - Total deaths
  - Total vaccinations
  
- Trends show:
  - Rapid growth in cases and deaths in 2020–2021.
  - Vaccinations began in early 2021 and ramped up globally.
  - By 2023, most countries reached a plateau in new cases and vaccinations.

---

## 3. Daily New Cases Comparison

- Compared **daily new COVID-19 cases** across selected countries.
- **Line plots** reveal:
  - Peaks occurred at different times by region.
  - India and the U.S. experienced some of the sharpest spikes.
  - Germany and South Africa showed more consistent wave patterns.

---

## 4. Death Rate Comparison

- **Death Rate** calculated as:  
  `death_rate = total_deaths / total_cases`

- Focused on the **peak pandemic year: 2022**
- **Bar charts** showed:
  - Peru and Egypt had higher estimated death rates.
  - Countries with higher vaccination and healthcare infrastructure had lower death rates.

---

## 5. Vaccination Rollout Analysis

### Cumulative Vaccinations Over Time
- **Line plots** for total vaccinations show:
  - United States and India led in raw numbers.
  - Growth in vaccinations tapered after 2022.

---

## Recommendations

- Compare vaccine rollout vs. case/death reduction.
- Analyze booster coverage across countries.
- Normalize metrics by age groups or population density.
- Create interactive maps of global trends.

---

