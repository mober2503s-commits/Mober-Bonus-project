import streamlit as st

# ---------------- LOGIC FUNCTIONS ---------------- #

def convert_height_to_meters(height, unit):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")

    if unit == "Centimeters (cm)":
        return height / 100
    elif unit == "Inches (in)":
        return height * 0.0254


def convert_weight_to_kg(weight, unit):
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    if unit == "Kilograms (kg)":
        return weight
    elif unit == "Pounds (lb)":
        return weight * 0.453592


def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)


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

st.title("⚖️ Smart BMI Calculator")

st.write("Enter your height and weight in any units")

# Unit selectors
height_unit = st.selectbox("Select Height Unit", ["Centimeters (cm)", "Inches (in)"])
weight_unit = st.selectbox("Select Weight Unit", ["Kilograms (kg)", "Pounds (lb)"])

# Inputs
height = st.number_input(f"Enter Height ({height_unit})", min_value=0.0, format="%.2f")
weight = st.number_input(f"Enter Weight ({weight_unit})", min_value=0.0, format="%.2f")

# Button
if st.button("Calculate BMI"):

    try:
        # Convert everything to metric system
        height_m = convert_height_to_meters(height, height_unit)
        weight_kg = convert_weight_to_kg(weight, weight_unit)

        bmi = calculate_bmi(weight_kg, height_m)
        category = bmi_category(bmi)

        st.success(f"Your BMI is: {bmi}")
        st.info(f"Health Category: {category}")

    except ValueError as e:
        st.error(str(e))


        #This is the website https://moberawanbmi.streamlit.app/.
