# 🚗 Used Car Price Prediction

This project uses machine learning to predict the **selling price of used cars** based on various features such as year, kilometers driven, fuel type, seller type, transmission, and ownership history.

---

## 📌 Objective

The goal of this project is to:

* Analyze a real-world dataset of used cars
* Perform data preprocessing and feature engineering
* Train multiple regression models
* Compare their performance
* Build a simple web app using Streamlit for real-time predictions

---

## 📊 Dataset

The dataset contains **4340 records** with the following features:

* **name** – Car name
* **year** – Year of manufacture
* **selling_price** – Selling price (target variable)
* **km_driven** – Kilometers driven
* **fuel** – Fuel type (Petrol, Diesel, etc.)
* **seller_type** – Dealer / Individual / Trustmark Dealer
* **transmission** – Manual / Automatic
* **owner** – Ownership history

---

## ⚙️ Project Workflow

1. Data loading
2. Data cleaning and preprocessing
3. Encoding categorical variables
4. Feature engineering

   * Created **car_age = 2026 - year**
5. Exploratory Data Analysis (EDA)
6. Train-test split
7. Model training:

   * Linear Regression
   * Lasso Regression
   * Random Forest Regressor
8. Model evaluation
9. Model comparison
10. Final model selection
11. Model saving
12. Streamlit app development

---

## 🧠 Models Used

* **Linear Regression**
* **Lasso Regression**
* **Random Forest Regressor (Final Model)**

---

## 📈 Evaluation Metrics

Models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🏆 Results

* Linear Regression and Lasso Regression showed moderate performance
* **Random Forest Regressor achieved the best performance**
* Final model achieved approximately:

```text
R² Score ≈ 0.69
```

👉 Random Forest was selected as the final model due to better generalization.

---

## 💡 Feature Engineering

A new feature was created:

```python
car_age = 2026 - year
```

This improved model performance compared to using raw year.

---

## 🖥️ Streamlit App

A simple web application was built using Streamlit.

### Features:

* User inputs car details
* Model predicts selling price instantly
* Easy-to-use interface

### Run the app:

```bash
streamlit run app.py
```

---

## ▶️ Usage

1. Run the notebook to understand the workflow
2. Run the Streamlit app for predictions

---

## 🚀 Future Improvements

* Hyperparameter tuning for Random Forest
* Try advanced models (XGBoost, Gradient Boosting)
* Deploy the app online (Streamlit Cloud)
* Add more features for better accuracy

---

