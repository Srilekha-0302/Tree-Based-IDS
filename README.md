# 🛡️ Tree-Based Intrusion Detection System

A modern Machine Learning-based Intrusion Detection System (IDS) built using tree-based ensemble models and deployed with an interactive Streamlit dashboard for real-time cyber attack detection.

---

# 📌 Overview

This project implements a **multi-phase Intrusion Detection System (IDS)** using classical and ensemble-based machine learning models trained on the **CICIDS2017 dataset**.

The system detects malicious network traffic and classifies multiple attack categories such as:

- DoS
- BruteForce
- WebAttack
- PortScan
- Bot
- Infiltration
- BENIGN traffic

The project follows a structured pipeline involving:

- Data preprocessing
- Feature selection
- SMOTE oversampling
- Tree-based model training
- Ensemble learning
- Real-time prediction dashboard using Streamlit

---

# 🚀 Features

✅ Real-time cyber attack prediction  
✅ Interactive Streamlit dashboard  
✅ Upload custom CSV network traffic data  
✅ Attack distribution visualization  
✅ Prediction confidence scores  
✅ Download prediction results as CSV  
✅ Feature-selected optimized model  
✅ Modern light-themed responsive UI  

---

# 🧠 Machine Learning Pipeline

## Phase 1 — Baseline Model Training
Trained multiple tree-based models on the CICIDS2017 dataset:

- Decision Tree
- Random Forest
- XGBoost

---

## Phase 2 — Feature Selection + SMOTE
Improved model performance through:

- Feature importance ranking
- Top feature selection
- SMOTE oversampling for class imbalance handling

---

## Phase 3 — Ensemble Learning
Implemented stacked ensemble learning using:

### Base Models
- Decision Tree
- Random Forest
- XGBoost

### Meta Learner
- Logistic Regression

---

# 📊 Model Performance

| Model | Accuracy |
|---|---|
| Decision Tree | 99.55% |
| Random Forest | 99.66% |
| XGBoost | 99.45% |
| Stacked Ensemble | **99.72%** |

## 📂 Project Structure
IDS-TreeBased/

├── data/ # Dataset files

├── notebooks/ # Jupyter notebooks for training and evaluation

├── models/ # Saved trained models (.pkl)

├── app.py

├── results/ # Confusion matrices, comparison tables, plots, UI

├── documentation.docx # Project Documentation

├── README.md # Project documentation

├── requirements.txt # Python dependencies

---

## 📊 Dataset
- **Dataset Used:** CICIDS2017  
- **Source:** [Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/ids-2017.html)  
- Contains both benign and multiple types of malicious network traffic.  
- Preprocessing steps included **label encoding** and **normalization**.

---

## 🛠️ Tools and Technologies
- **Languages:** Python 
- **Libraries:** NumPy, Pandas, Scikit-learn, XGBoost, Imbalanced-learn, Seaborn, Matplotlib, Joblib  
- **Development Tools:** Jupyter Notebook, VS Code, Google Colab

# 🖥️ Dashboard UI

## Home Interface

![Home UI](results/UI/home_ui.png)

---

## Analytics Dashboard

![Dashboard](results/UI/dashboard.png)

---

## Prediction Results

![Prediction Results](results/UI/prediction_results.png)

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/Srilekha-0302/Tree-Based-IDS.git
cd Tree-Based-IDS

# Install dependencies
pip install -r requirements.txt

# Run Streamlit App
streamlit run app.py

