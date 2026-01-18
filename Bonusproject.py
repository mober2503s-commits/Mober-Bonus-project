import streamlit as st

# ---------------- LOGIC FUNCTIONS ---------------- #

def convert_height_to_meters(height, unit):
    """
    CDC standard conversions
    https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")

    if unit == "Centimeters (cm)":
        return height / 100
    elif unit == "Inches (in)":
        return height * 0.0254


def convert_weight_to_kg(weight, unit):
    """
    CDC standard conversions
    https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
    """
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    if unit == "Kilograms (kg)":
        return weight
    elif unit == "Pounds (lb)":
        return weight * 0.453592


def calculate_bmi(weight_kg, height_m):
    """
    WHO BMI Formula
    BMI = kg / m²
    https://www.who.int/data/gho/data/themes/theme-details/GHO/body-mass-index
    """
    return round(weight_kg / (height_m ** 2), 2)


def bmi_category(bmi):
    """
    WHO BMI Classification
    https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# ---------------- UI DESIGN ---------------- #

st.set_page_config(page_title="BMI Calculator", page_icon="🏃")

st.title("🏃 Smart BMI Calculator (Medically Accurate)")

height_unit = st.selectbox("Height Unit", ["Centimeters (cm)", "Inches (in)"])
weight_unit = st.selectbox("Weight Unit", ["Kilograms (kg)", "Pounds (lb)"])

height = st.number_input(f"Height ({height_unit})", min_value=0.0, format="%.2f")
weight = st.number_input(f"Weight ({weight_unit})", min_value=0.0, format="%.2f")

if height > 0 and weight > 0:
    try:
        # STEP 1: Convert to medical standard units
        height_m = convert_height_to_meters(height, height_unit)
        weight_kg = convert_weight_to_kg(weight, weight_unit)

        # STEP 2: Apply WHO BMI formula
        bmi = calculate_bmi(weight_kg, height_m)
        category = bmi_category(bmi)

        st.success(f"BMI: {bmi}")
        st.info(f"Category: {category}")

    except ValueError as e:
        st.error(str(e))






        #This is the website https://moberawanbmi.streamlit.app/.
