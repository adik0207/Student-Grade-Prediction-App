# 🎓 Student Grade Prediction App

This project is a Machine Learning-based web application that predicts a student’s **final grade (G3)** using various academic and personal attributes. The model is built using **Random Forest Regressor**, and the interface is built with **Streamlit** for real-time predictions.

---

## 🚀 Demo

🖥️ Streamlit App Screenshot  
![image](https://github.com/user-attachments/assets/72ee586b-3ab5-4a44-ad2f-f353e8c367fb)


---

## 📂 Dataset

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
- File: `student-mat.csv`  
- Description: Data includes student academic records and personal background attributes such as:
  - Past grades (G1, G2)
  - Study time
  - Internet access
  - Parental education
  - Family support
  - Absences

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Regressor  
- **Target Variable**: G3 (Final Grade)  
- **Feature Engineering**:
  - Label Encoding for categorical variables
  - No missing values or nulls
- **Evaluation Metrics**:
  - MAE: ~1.10  
  - RMSE: ~1.87  
  - R² Score: ~83%

---

## 📊 EDA Highlights

- G1 & G2 (past grades) show the highest correlation with G3
- Higher study time generally leads to better final grades
- Internet access and parental education show moderate influence

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
- Streamlit (Web App)
- Joblib & Pickle (Model + Preprocessor Saving)

---

## 📦 Project Structure

├── app.py # Streamlit app ├── student-mat.csv # Dataset ├── grade_predictor.pkl # Trained model ├── label_encoders.pkl # Encoders for categorical features ├── columns.pkl # Saved column order ├── README.md # Project readme └── requirements.txt # Project dependencies

---

## 🧪 How to Run Locally

1. **Clone the repo**
   
git clone https://github.com/your-username/student-grade-predictor.git
cd student-grade-predictor

Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app.py

✨ Features
Real-time prediction based on user input

Intuitive UI with dropdowns and sliders

Easy to extend or retrain on new data

Visual feature importance and EDA insights

📌 Use Cases
Useful for teachers and education administrators

Helps in identifying students needing intervention

Can be integrated into school management systems

🙋‍♂️ Author
Aditya Khare
Developer | Data Enthusiast
📧 adikhare0207@gmail.com

🌟 Star this repo if you found it useful!
