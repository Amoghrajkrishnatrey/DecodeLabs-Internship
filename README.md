# E-Commerce Exploratory Data Analysis (EDA) & Business Insights

An exploratory data analysis script designed to analyze order volumes, calculate order cancellation rates, handle missing values, detect high-value revenue outliers using the Interquartile Range (IQR) method, and generate insightful visualizations.

## Project Overview

This script processes e-commerce order data to extract critical business insights:
- **Data Cleaning:** Imputes missing coupon code values with a standard default (`NO_COUPON`).
- **Cancellation Analysis:** Calculates the overall order cancellation percentage to highlight operational friction.
- **Outlier Detection:** Applies the IQR statistical method to identify high-value transaction outliers on `TotalPrice`.
- **Visual Analytics:** Generates a dual-panel dashboard using Matplotlib and Seaborn showing:
  1. Order volume breakdown by status.
  2. Revenue distribution skewness with a median reference indicator.

## Requirements

Ensure you have Python 3.x installed along with the required libraries:

```bash
pip install pandas matplotlib seaborn openpyxl
