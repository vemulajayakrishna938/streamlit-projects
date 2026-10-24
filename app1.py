import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="User Registration Form",
    page_icon="📝",
    layout="centered"
)

# Application title
st.title("📝 User Registration Form")
st.write("Please fill in your details below.")

st.divider()

# Create a user form
with st.form("user_registration_form"):

    # Username
    username = st.text_input("Username", placeholder="Enter your username")

    # Email
    email = st.text_input("Email Address", placeholder="example@gmail.com")

    # Phone number
    phone = st.text_input("Phone Number", placeholder="Enter your 10-digit phone number")

    # First and last name
    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name", placeholder="Enter first name")

    with col2:
        last_name = st.text_input("Last Name", placeholder="Enter last name")

    # Slot timing
    slot_timing = st.selectbox(
        "Select Slot Timing",
        [
            "Select a slot",
            "09:00 AM - 10:00 AM",
            "10:00 AM - 11:00 AM",
            "11:00 AM - 12:00 PM",
            "02:00 PM - 03:00 PM",
            "03:00 PM - 04:00 PM",
            "04:00 PM - 05:00 PM"
        ]
    )

    # Submit button
    submitted = st.form_submit_button(
        "Register",
        use_container_width=True
    )

# Process submitted form
if submitted:

    # Check required fields
    if not all([
        username.strip(),
        email.strip(),
        phone.strip(),
        first_name.strip(),
        last_name.strip()
    ]):
        st.error("Please fill in all the fields.")

    # Validate email
    elif not re.fullmatch(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        email.strip()
    ):
        st.error("Please enter a valid email address.")

    # Validate phone number
    elif not re.fullmatch(r"\+?[0-9]{10,15}", phone.strip()):
        st.error("Enter a valid phone number with 10-15 digits.")

    # Validate slot
    elif slot_timing == "Select a slot":
        st.error("Please select a slot timing.")

    else:
        st.success("Registration successful!")

        st.subheader("Submitted User Details")

        st.write(f"**Username:** {username}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone Number:** {phone}")
        st.write(f"**First Name:** {first_name}")
        st.write(f"**Last Name:** {last_name}")
        st.write(f"**Slot Timing:** {slot_timing}")

        st.info("Your details have been submitted successfully.")