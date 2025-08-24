import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import plotly.graph_objects as go

# ---- Page Config ----
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="wide"
)

# ---- Sidebar ----
st.sidebar.title("🫀 Heart Disease Predictor")
st.sidebar.markdown(
    """
    Estimate the **likelihood of heart disease** based on patient health metrics.
    """
)

st.sidebar.subheader("⚙️ Model Details")
st.sidebar.markdown(
    """
    - Algorithm: Trained ML classifier  
    - Features: Age, Cholesterol, BP, ECG, etc.  
    - Output: Binary prediction + probability score
    """
)

st.sidebar.subheader("⚠️ Disclaimer")
st.sidebar.info(
    "This app is **for educational/demo purposes only**. "
    "It is **not a medical diagnostic tool**. "
    "Always consult qualified healthcare professionals."
)

# ---- Load Model ----
MODEL_PATH = Path("trained_model.sav")
if not MODEL_PATH.exists():
    st.error("❌ trained_model.sav not found. Please place it in the same directory.")
    st.stop()

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

FEATURE_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

# ---- Healthy Reference Ranges ----
HEALTHY_RANGES = {
    "age": 30,
    "trestbps": 120,
    "chol": 200,
    "thalach": 170,
    "oldpeak": 0.0
}

# ---- Header ----
st.title("🩺 Heart Disease Prediction Tool")
st.caption("Fill in patient details to predict the likelihood of heart disease.")

# ---- Input Form ----
with st.form("input_form"):
    st.subheader("Patient Clinical Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=45, step=1)
        sex = st.selectbox("Sex", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3],
                          format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal", "Asymptomatic"][x])
        trestbps = st.number_input("Resting BP (mm Hg)", min_value=50, max_value=250, value=130)

    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=80, max_value=650, value=246)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        restecg = st.selectbox("Resting ECG Results", [0, 1, 2],
                               format_func=lambda x: ["Normal", "ST-T abnormality", "LV Hypertrophy"][x])
        thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=250, value=150)

    with col3:
        exang = st.selectbox("Exercise Induced Angina", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        slope = st.selectbox("Slope of ST Segment", [0, 1, 2],
                             format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
        ca = st.selectbox("Major Vessels Colored (0-4)", [0, 1, 2, 3, 4])
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3],
                            format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect", "Other"][x])

    submitted = st.form_submit_button("🔍 Predict")

# ---- Prediction ----
if submitted:
    row = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    X_infer = pd.DataFrame([row], columns=FEATURE_NAMES)

    try:
        pred = model.predict(X_infer)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(X_infer)[0][1])

        st.divider()
        st.subheader("📊 Prediction Result")

        # Probability display
        if proba is not None:
            st.metric(label="Probability of Heart Disease", value=f"{proba:.1%}")

            # ---- Gauge Chart ----
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=proba * 100,
                title={'text': "Risk Level (%)"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkred"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgreen"},
                        {'range': [30, 60], 'color': "yellow"},
                        {'range': [60, 100], 'color': "tomato"}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': proba * 100
                    }
                }
            ))
            st.plotly_chart(fig, use_container_width=True)

        # ---- Radar Chart ----
        st.subheader("📈 Patient Profile vs Healthy Ranges")

        categories = list(HEALTHY_RANGES.keys())
        patient_values = [
            age,
            trestbps,
            chol,
            thalach,
            oldpeak
        ]
        healthy_values = list(HEALTHY_RANGES.values())

        radar_fig = go.Figure()

        radar_fig.add_trace(go.Scatterpolar(
            r=patient_values,
            theta=categories,
            fill='toself',
            name='Patient'
        ))

        radar_fig.add_trace(go.Scatterpolar(
            r=healthy_values,
            theta=categories,
            fill='toself',
            name='Healthy Reference'
        ))

        radar_fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, max(max(patient_values), max(healthy_values)) + 20])
            ),
            showlegend=True
        )

        st.plotly_chart(radar_fig, use_container_width=True)

        # Textual output
        if int(pred) == 1:
            st.error("⚠️ Patient **likely has Heart Disease**")
        else:
            st.success("✅ Patient **likely does not have Heart Disease**")

    except Exception as e:
        st.exception(e)
        st.stop()
