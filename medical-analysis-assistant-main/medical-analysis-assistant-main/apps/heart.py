import pandas as pd
import streamlit as st
from joblib import load
from sklearn.linear_model import LogisticRegression

def load_heart_model():
    return load("models/heart.joblib")

def heart_page():
    model = load_heart_model()
    st.subheader("Heart Disease Prediction", divider='grey')

    st.caption("Input Details")

    col1, col2,  = st.columns(2, gap='large')
    age = col1.number_input("Age", min_value=29, max_value=77, value=50, step=1)
    trestbps = col1.number_input("Resting Blood Pressure", min_value=94, max_value=200, value=120, step=1)
    chol = col1.number_input("Serum Cholesterol", min_value=126, max_value=564, value=240, step=1)
    thalach = col1.number_input("Maximum Heart Rate Achieved", min_value=71, max_value=202, value=150, step=1)
    oldpeak = col1.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=6.2, value=1.0, step=0.1)
    ca = col1.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, value=1, step=1)

    sex = col2.selectbox("Sex", ["Male", "Female"])
    cp = col2.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    fbs = col2.selectbox("Fasting Blood Sugar", ["Lower than 120 mg/dl", "Greater than 120 mg/dl"])
    restecg = col2.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Probable or Definite Left Ventricular Hypertrophy"])
    exang = col2.selectbox("Exercise Induced Angina", ["Yes", "No"])
    slope = col2.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    thal = col2.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

  
    sex = 1 if sex == "Male" else 0
    cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
    cp = cp_mapping[cp]
    fbs = 1 if fbs == "Greater than 120 mg/dl" else 0
    restecg_mapping = {"Normal": 0, "ST-T Wave Abnormality": 1, "Probable or Definite Left Ventricular Hypertrophy": 2}
    restecg = restecg_mapping[restecg]
    exang = 1 if exang == "Yes" else 0
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}
    thal = thal_mapping[thal]

    user_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    })
    
    st.markdown('')
    if st.button("Predict"):
        prediction = model.predict(user_data)

        st.subheader("Prediction Result:")
        if prediction[0] == 1:
            st.write("The model predicts that the person likely has a heart disease.")
        else:
            st.write("The model predicts that the person likely does not have a heart disease.")

if __name__ == "__main__":
    heart_page()
