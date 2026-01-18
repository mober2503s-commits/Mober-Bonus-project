import streamlit as st

# ---------------- LOGIC FUNCTIONS ---------------- #

def convert_height_to_meters(height, unit):
    """
    Converts height to meters using CDC standard conversions
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")

    conversion = {
        "Centimeters (cm)": height / 100,
        "Inches (in)": height * 0.0254
    }

    return conversion.get(unit)


def convert_weight_to_kg(weight, unit):
    """
    Converts weight to kilograms using CDC standard conversions
    """
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    conversion = {
        "Kilograms (kg)": weight,
        "Pounds (lb)": weight * 0.453592
    }

    return conversion.get(unit)


def calculate_bmi(weight_kg, height_m):
    """
    WHO BMI Formula:
    BMI = weight (kg) / height (m)^2
    """
    return round(weight_kg / (height_m ** 2), 2)


def bmi_category(bmi):
    """
    WHO BMI Classification
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

st.title("🏃 Smart BMI Calculator")
st.write("Enter your height and weight in any unit system")

# Unit selectors
col1, col2 = st.columns(2)

with col1:
    height_unit = st.selectbox("Height Unit", ["Centimeters (cm)", "Inches (in)"])

with col2:
    weight_unit = st.selectbox("Weight Unit", ["Kilograms (kg)", "Pounds (lb)"])

# Inputs
height = st.number_input(f"Height ({height_unit})", min_value=0.0, format="%.2f")
weight = st.number_input(f"Weight ({weight_unit})", min_value=0.0, format="%.2f")

# Auto calculation when values are entered
if height > 0 and weight > 0:

    try:
        height_m = convert_height_to_meters(height, height_unit)
        weight_kg = convert_weight_to_kg(weight, weight_unit)

        bmi = calculate_bmi(weight_kg, height_m)
        category = bmi_category(bmi)

        st.subheader("📊 Result")
        st.success(f"BMI: {bmi}")
        st.info(f"Category: {category}")

    except ValueError as e:
        st.error(str(e))
else:
    st.warning("Please enter both height and weight.")




        #This is the website https://moberawanbmi.streamlit.app/.
