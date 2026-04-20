# 💳 Credit Card Fraud Detection System (ML + Deployment)

## 🚀 Live App

👉 https://fraud-detection-app-jx26ld2ghv2qv3qnhkaykr.streamlit.app/

---

## 📌 Project Overview

This project builds a machine learning model to detect fraudulent credit card transactions and deploys it as an interactive web application.

Users can input transaction details and instantly receive predictions on whether the transaction is **fraudulent or safe**.

---

## 🎯 Problem Statement

Credit card fraud is a major challenge in the financial industry. The objective of this project is to:

* Accurately detect fraudulent transactions
* Handle imbalanced datasets
* Provide real-time predictions through a web interface

---

## 📊 Workflow

### 1️⃣ Data Analysis

* Checked missing values and duplicates
* Performed exploratory data analysis (EDA)
* Visualized fraud vs non-fraud distribution

### 2️⃣ Data Preprocessing

* Feature selection
* Handled class imbalance using SMOTE
* Train-test split

### 3️⃣ Model Building

Trained and compared multiple models:

* Logistic Regression
* Random Forest
* K-Nearest Neighbors (KNN)

👉 Selected the best-performing model based on accuracy and performance metrics.

---

## 📈 Model Performance

* Accuracy: **~98%**
* Precision: High fraud detection capability
* Recall: Strong detection of fraudulent transactions

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Streamlit

---

## 🌐 Deployment

The model is deployed using Streamlit Cloud, allowing users to interact with the model through a web-based interface.

---

## 📁 Project Structure

```
Credit Card Fraud Detection/
│
├── app.py                 # Streamlit web app
├── fraud_model.pkl        # Trained ML model
├── notebook.ipynb         # EDA + Model training
├── requirements.txt       # Dependencies
└── data/                  # Dataset (optional)
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/fraud-detection-app.git
cd fraud-detection-app
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 💡 Key Learnings

* Handling imbalanced datasets using SMOTE
* Building and comparing ML models
* Creating an end-to-end ML pipeline
* Deploying ML models using Streamlit

---

## 💼 Resume Highlight

Developed and deployed a credit card fraud detection system using machine learning and Streamlit, enabling real-time fraud prediction with high accuracy.

---

