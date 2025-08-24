# 🫀 Heart Disease Prediction Web App

A user-friendly web application built with Streamlit to predict the likelihood of heart disease using a trained machine learning model. This tool provides instant predictions and visual feedback based on patient clinical data.

---

### 🚀 [Live Demo Link](http://localhost:8501/)

---

## ✨ Key Features

-   **Interactive Patient Form**: A clean and simple form to input 13 different clinical features.
-   **Real-Time Prediction**: Instantly get a binary prediction (Disease/No Disease) and a precise probability score.
-   **Rich Data Visualization**:
    -   A **Risk Gauge** chart to visually represent the probability of heart disease.
    -   A **Radar Chart** to compare the patient's key metrics against healthy reference values.

---

## 📸 Application Screenshots

| Input Form | Prediction Result |
| :---: | :---: |
| ![Input Form](https://github.com/aryaktc/Heart-Disease-Prediction-Model/blob/main/images/Screenshot%202025-08-24%20220300.png?raw=true) | ![Prediction Result](https://github.com/aryaktc/Heart-Disease-Prediction-Model/blob/main/images/Screenshot%202025-08-24%20220338.png?raw=true) |
| **Patient Profile Analysis** |
| ![Patient Profile](https://github.com/aryaktc/Heart-Disease-Prediction-Model/blob/main/images/Screenshot%202025-08-24%20220403.png?raw=true) |

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
    git clone [https://github.com/aryaktc/Heart-Disease-Prediction-Model.git](https://github.com/aryaktc/Heart-Disease-Prediction-Model.git)
    cd Heart-Disease-Prediction-Model
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
