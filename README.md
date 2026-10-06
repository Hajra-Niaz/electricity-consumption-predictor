\# ⚡ Electricity Consumption Predictor



\## 📌 Project Overview

This is a practice project built during my AI learning journey. It is an end-to-end Machine Learning web application that predicts the \*\*next month's electricity consumption (kWh)\*\* for a household based on environmental and household data.



The goal is to help with demand forecasting and energy management by estimating future usage based on temperature, number of residents, and past consumption.



\## 📊 Dataset

\- \*\*File:\*\* `electricity\_consumption\_forecast.csv`

\- \*\*Records:\*\* 1,000 rows, 5 columns

\- \*\*Features:\*\*

&#x20; - `Month` (1-12)

&#x20; - `Avg\_Temperature\_C` (5°C to 45°C)

&#x20; - `Residents` (Number of people in the house)

&#x20; - `Past\_Month\_Consumption\_kWh`

\- \*\*Target:\*\* `Next\_Month\_Consumption\_kWh`



\## 🛠️ Tools \& Technologies Used

\- \*\*Python\*\* (Pandas, NumPy)

\- \*\*Scikit-learn\*\* (Linear Regression)

\- \*\*Joblib\*\* (Model saving/loading)

\- \*\*Streamlit\*\* (Interactive web app)

\- \*\*Jupyter Notebook\*\* (EDA \& Model Training)



\## ⚙️ Machine Learning Pipeline

1\. \*\*Data Loading \& Preprocessing:\*\* Loaded the CSV and separated features (X) and target (y).

2\. \*\*Train/Test Split:\*\* 70% training, 30% testing (`random\_state=42`).

3\. \*\*Model:\*\* Trained a `LinearRegression` model.

4\. \*\*Model Persistence:\*\* Saved the trained model as `elec.pkl` using `joblib`.



\## 🚀 How to Run the Web App Locally

1\. Clone this repository.

2\. Install the requirements:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

