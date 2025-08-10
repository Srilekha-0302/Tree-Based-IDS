# Intrusion Detection System using Tree-Based Machine Learning Models
Multi-phase Intrusion Detection System using Decision Tree, Random Forest, and XGBoost on the CICIDS2017 dataset with feature selection, SMOTE oversampling, and stacked ensemble learning.

## 📌 Overview
This project implements a **multi-phase Intrusion Detection System (IDS)** using classical tree-based machine learning models. It is designed to detect malicious network activity using the **CICIDS2017** dataset, following a structured three-phase pipeline:  
1. **Phase 1:** Baseline training of Decision Tree, Random Forest, and XGBoost models.  
2. **Phase 2:** Feature selection and **SMOTE oversampling** to handle class imbalance.  
3. **Phase 3:** **Stacked Ensemble Learning** for improved accuracy and generalization.  

The system is evaluated using **accuracy, precision, recall, F1-score**, confusion matrices, and **time efficiency analysis**.

---

## 📂 Project Structure
IDS-TreeBased/

├── data/ # Dataset files

├── notebooks/ # Jupyter notebooks for training and evaluation

├── models/ # Saved trained models (.pkl)

├── results/ # Confusion matrices, comparison tables, plots

├── README.md # Project documentation

├── requirements.txt # Python dependencies


---

## 📊 Dataset
- **Dataset Used:** CICIDS2017  
- **Source:** [Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/ids-2017.html)  
- Contains both benign and multiple types of malicious network traffic.  
- Preprocessing steps included **label encoding** and **normalization**.

---

## ⚙️ Methodology

### **Phase 1 – Model Training**
- Models: **Decision Tree**, **Random Forest**, **XGBoost**
- Trained on the preprocessed dataset without feature reduction.

### **Phase 2 – Feature Selection + SMOTE**
- Features ranked by average importance from all models.  
- Selected features covering **90% cumulative importance**.  
- **SMOTE** applied to balance underrepresented classes (e.g., Infiltration attacks).

### **Phase 3 – Stacked Ensemble**
- Base models: Decision Tree, Random Forest, XGBoost.  
- Meta-learner: **Logistic Regression**.  
- Achieved the **highest accuracy** among all models.

---

## 📈 Results
| Model              | Accuracy  | Precision | Recall  | F1-score |
|--------------------|-----------|-----------|---------|----------|
| Decision Tree (P2) | 99.55%    | 99.55%    | 99.55%  | 99.55%   |
| Random Forest (P2) | **99.66%**| **99.66%**| **99.66%**| **99.66%**|
| XGBoost (P2)       | 99.45%    | 99.45%    | 99.45%  | 99.45%   |
| Stacked Ensemble   | **99.72%**| **99.72%**| **99.72%**| **99.72%**|

---

## 🛠️ Tools and Technologies
- **Languages:** Python 3.10+  
- **Libraries:** NumPy, Pandas, Scikit-learn, XGBoost, Imbalanced-learn, Seaborn, Matplotlib, Joblib  
- **Development Tools:** Jupyter Notebook, VS Code  
- **OS:** Windows 10 / Ubuntu 20.04 LTS  

---

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/Srilekha-0302/Tree-Based-IDS.git
cd IDS-TreeBased

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/IDS_SSL.ipynb

