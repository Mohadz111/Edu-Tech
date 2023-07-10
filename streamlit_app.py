import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import requests
from io import BytesIO

# Load the model
model_url = 'https://github.com/Mohadz111/Edu-Tech/raw/master/RandomForestModel.pkl'
response = requests.get(model_url)
loaded_model = joblib.load(BytesIO(response.content))

# Load the training data
data_url = 'https://github.com/Mohadz111/Edu-Tech/raw/master/Dataset.csv'
training_data = pd.read_csv(data_url)

# Extract the categorical columns
categorical_columns = ['Course', 'Level', 'Marital', 'Gender']

# Define the mapping for categorical values
mapping = {
    'Course': {'EDT 400': 0, 'EDT 200': 1},
    'Level': {'400': 0, '200': 1},
    'Marital': {'Married': 0, 'Single': 1},
    'Gender': {'Male': 0, 'Female': 1}
}

# Create the Streamlit app
def main():
    st.title("An Educational Technology Prediction Model Designed Specifically for Undergraduate Students")

    # Sidebar input form
    st.sidebar.header("Enter Data")
    course_values = ['EDT 400', 'EDT 200']
    level_values = ['400', '200']
    marital_values = ['Married', 'Single']
    gender_values = ['Male', 'Female']
    course = st.sidebar.selectbox("Course", course_values)
    level = st.sidebar.selectbox("Level", level_values)
    marital = st.sidebar.selectbox("Marital Status", marital_values)
    gender = st.sidebar.selectbox("Gender", gender_values)
    age = st.sidebar.slider("Age", 0, 100, 25)
    test = st.sidebar.slider("Test Score", 0.0, 100.0, 50.0)

    # Prepare input data
    input_data = pd.DataFrame({
        "Course": [mapping['Course'][course]],
        "Level": [mapping['Level'][level]],
        "Marital": [mapping['Marital'][marital]],
        "Gender": [mapping['Gender'][gender]],
        "Age": [age],
        "Test": [test]
    })

    # Make prediction for Exam
    exam_prediction = loaded_model.predict(input_data)

    # Calculate Total as sum of Test and Exam
    total_prediction = test + exam_prediction

    # Display predictions
    st.subheader("Exam Prediction")
    st.write(f"The predicted Exam value is: {exam_prediction}")

    st.subheader("Total Prediction")
    st.write(f"The predicted Total value is: {total_prediction}")


if __name__ == "__main__":
    main()
