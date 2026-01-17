import streamlit as st

# ---------------- LOGIC FUNCTIONS ---------------- #

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# ---------------- UI DESIGN ---------------- #

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ BMI Calculator")
st.write("Enter your details to calculate your Body Mass Index")

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (meters)", min_value=0.0, format="%.2f")

# Button
if st.button("Calculate BMI"):

    try:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        st.success(f"Your BMI is: {bmi}")
        st.info(f"Category: {category}")

    except ValueError as e:
        st.error(str(e))
        #This is the website https://moberawanbmi.streamlit.app/.
