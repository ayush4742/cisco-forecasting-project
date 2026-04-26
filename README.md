# 🚀 Cisco Forecasting Project

## 📌 Overview

This project forecasts **FY26 Q2 demand** for networking products using historical quarterly sales data.
The goal is to produce **realistic, business-usable predictions** that help in inventory planning, cost control, and decision-making.

---

## 🎯 Problem Statement

Given product-wise sales from **FY23 Q2 → FY26 Q1**, predict **FY26 Q2 demand** accurately while preserving real-world trends (no unrealistic spikes/drops).

---

## 📊 Dataset

* Rows: Networking products (Switches, Routers, Wireless, etc.)
* Columns: Quarterly sales (FY23 Q2 → FY26 Q1)
* Target: **FY26 Q2**

**Challenges:**

* Missing values
* High variance across products
* Different demand behaviors (stable vs volatile)

---

## 🔍 Exploratory Data Analysis (EDA)

* Cleaned missing values using **forward fill (time-series aware)**
* Checked distribution & outliers across quarters
* Compared product categories (Wireless, Switches, etc.)
* Identified:

  * High-demand vs low-demand products
  * Stable vs volatile trends

---

## ⚙️ Feature Engineering

To capture demand behavior:

* **Lag Features** → Recent demand signal (last quarter)
* **Trend Features** → Growth/decline over time
* **Rolling Mean** → Smooth noise
* **Average Demand** → Stability indicator
* **Volatility** → Demand fluctuation measure

👉 These features help the model **understand pattern, not just numbers**

---

## 🤖 Model Approach

### Models Used

* **Random Forest**

  * Robust, handles noise well
* **XGBoost**

  * Captures complex non-linear relationships

### Ensemble Strategy

Predictions combined using weighted average:

```bash
y_pred = 0.4 * RF + 0.6 * XGB
```

✔ Improves generalization
✔ Reduces overfitting
✔ Produces stable predictions

---

## 🧠 Business Logic Layer (Key Differentiator)

Machine learning alone is not enough.
We applied **post-processing rules** to make predictions realistic:

* 🚫 Removed negative values
* 📉 Controlled unrealistic spikes
* 📈 Ensured predictions follow trend direction
* 🔄 Smoothed extreme variations

👉 This step ensures **real-world usability**, not just model accuracy.

---

## 📈 Results

* Stable and consistent predictions
* High-demand products maintained strong signals
* Low-demand products remained realistic (no noise spikes)
* Ensemble model outperformed individual models

---

## 🔎 Key Insights

* 📡 **Wireless products show highest demand**
* 🔁 Core infrastructure (Switches/Routers) remains stable
* 📊 Trend-based features significantly improved prediction quality
* 🤝 Ensemble learning provided better balance than single models

---

## 📦 Output

Final predictions available at:

```bash
output/submission.csv
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Matplotlib

---

## 🏆 Achievement

Ranked among **200+ teams** in the Cisco Forecasting Challenge.

---

## 📬 Conclusion

This project demonstrates that **combining ML + business understanding** leads to better forecasting than using models alone.

👉 Focus was not only accuracy, but **realistic and explainable predictions**.

---

⭐ If you found this project useful, consider starring the repository!
