# 📉 Customer Churn Prediction using Machine Learning

## 📌 Overview
This project focuses on predicting **customer churn** using **Machine Learning**.  
Customer churn refers to customers who stop using a company’s services. Predicting churn helps businesses take proactive steps to **retain customers** and reduce revenue loss.

The project involves:
- Data preprocessing and analysis
- Training a machine learning classification model
- Building an interactive **Streamlit web application** for churn prediction

---

## 📂 Dataset
The dataset contains customer-related information used to predict whether a customer is likely to churn.

### Key Features
- Age
- Gender
- Tenure (months)
- Monthly Charges
- Churn (Target Variable)

The dataset is preprocessed before training the machine learning model.

---

## 🛠️ Tools & Technologies
- **Python**
  - Pandas
  - NumPy
  - Scikit-learn
- **Machine Learning**
  - Classification model
  - Feature scaling using StandardScaler
- **Streamlit**
  - Web application for real-time predictions
- **Joblib**
  - Model and scaler serialization

---

## 🔍 Project Workflow

### 1️⃣ Data Loading & Preprocessing
- Loaded customer churn dataset using Pandas.
- Handled categorical features (Gender encoding).
- Selected relevant features for model training.
- Scaled numerical features using **StandardScaler**.

---

### 2️⃣ Exploratory Data Analysis (EDA)
- Analyzed customer churn distribution.
- Studied relationships between tenure, monthly charges, and churn.
- Identified patterns affecting customer retention.

---

### 3️⃣ Model Training
- Trained a machine learning classification model on processed data.
- Evaluated model performance using accuracy metrics.
- Saved the trained model and scaler using **Joblib**.

---

### 4️⃣ Streamlit Web Application
A user-friendly Streamlit app was built to predict customer churn.

#### App Features
- User inputs:
  - Age
  - Gender
  - Tenure
  - Monthly Charges
- Scales inputs using saved scaler
- Predicts churn using trained ML model
- Displays result as **Yes / No**

---

## 🖥️ Application Preview
The Streamlit app allows users to enter customer details and instantly check whether the customer is likely to churn.

---

## ▶️ How to Run the Project

### 1️⃣ Take the dataset from the kaggle

### 2️⃣ Install Dependencies
    pip install pandas numpy scikit-learn streamlit joblib

### 3️⃣ Run the Streamlit App
    streamlit run app.py

---

### 📈 Results

- Successfully predicts customer churn based on input features.

- Helps identify high-risk customers.

- Can assist businesses in designing better customer retention strategies.

---

### 🚀 Future Improvements

- Add more customer behavioral features.

- Improve model accuracy using advanced algorithms.

- Add probability-based churn prediction.

- Deploy the application on cloud platforms.

---

### 📚 References

YouTube Tutorial: https://youtu.be/XRnQUQmS2_s?si=9Xe38_XPjjRhCdJW
