import streamlit as st



def calculate_bmi_kg_cm(weight_kg, height_cm):
    if height_cm <= 0:
        raise ValueError("Height must be greater than zero.")

    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)


def calculate_bmi_lb_in(weight_lb, height_in):
    if height_in <= 0:
        raise ValueError("Height must be greater than zero.")

    return round(703 * weight_lb / (height_in ** 2), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"



st.set_page_config(page_title="BMI Calculator", page_icon="🏃")

st.title("🔢 BMI Calculator")

st.write("Select your height and weight units")


height_unit = st.selectbox("Select Height Unit:", ["Centimeters (cm)", "Inches (in)"])
weight_unit = st.selectbox("Select Weight Unit:", ["Kilograms (kg)", "Pounds (lb)"])


weight = st.number_input(f"Enter your weight ({weight_unit})", min_value=0.0, format="%.2f")
height = st.number_input(f"Enter your height ({height_unit})", min_value=0.0, format="%.2f")


if st.button("Calculate BMI"):

    try:
       
        if weight_unit == "Kilograms (kg)" and height_unit == "Centimeters (cm)":
            bmi = calculate_bmi_kg_cm(weight, height)

        elif weight_unit == "Pounds (lb)" and height_unit == "Inches (in)":
            bmi = calculate_bmi_lb_in(weight, height)

        else:
            st.error("Please use matching units: kg with cm OR lb with inches.")
            st.stop()

        category = bmi_category(bmi)

        st.success(f"Your BMI is: {bmi}")
        st.info(f"Health Category: {category}")

    except ValueError as e:
        st.error(str(e))

 





        #This is the website https://moberawanbmi.streamlit.app/.
