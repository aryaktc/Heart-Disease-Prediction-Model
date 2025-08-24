# 🫀 Heart Disease Prediction Web App

A user-friendly web application built with Streamlit to predict the likelihood of heart disease using a trained machine learning model. This tool provides instant predictions and visual feedback based on patient clinical data.

![Heart Disease Predictor Screenshot](https://i.imgur.com/your-screenshot-url.png)
*(**Note:** Replace the URL above with a link to a screenshot of your running app for a complete profile.)*

---

## 📋 Project Overview

This project demonstrates a full end-to-end machine learning workflow, from data exploration and model training to deployment as an interactive web application. The core of the application is a Logistic Regression model trained on the Heart Disease UCI dataset to classify whether a patient is likely to have heart disease. The Streamlit front-end provides an intuitive interface for users to input data and receive real-time, visualized predictions.

---

## ✨ Key Features

-   **Interactive Patient Form**: A clean and simple form to input 13 different clinical features.
-   **Real-Time Prediction**: Instantly get a binary prediction (Disease/No Disease) and a precise probability score.
-   **Rich Data Visualization**:
    -   A **Risk Gauge** chart to visually represent the probability of heart disease.
    -   A **Radar Chart** to compare the patient's key metrics against healthy reference values.
-   **Detailed Sidebar**: Contains model details, project information, and a clear disclaimer on the app's educational purpose.

---

## 🛠️ Technology Stack

-   **Language**: Python
-   **Web Framework**: Streamlit
-   **Machine Learning**: Scikit-learn
-   **Data Manipulation**: Pandas
-   **Data Visualization**: Plotly

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Installation & Usage

1.  **Clone the GitHub repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/heart-disease-predictor.git](https://github.com/YOUR_USERNAME/heart-disease-predictor.git)
    cd heart-disease-predictor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

The application will automatically open in a new tab in your default web browser.

---

## 📂 Repository Structure

├── app.py                      # Main Streamlit application script├── trained_model.sav           # Pre-trained Logistic Regression model file├── Heart_disease_predictor.ipynb # Jupyter Notebook with the model training process├── heart_disease_data.csv      # The dataset used for training├── requirements.txt            # List of required Python packages└── README.md                   # Project documentation
---

## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes only**. It is **not a medical diagnostic tool** and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare professional for any medical concerns.
