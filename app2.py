
import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="Cricket Registration",
    page_icon="🏏",
    layout="centered"
)

# Application title
st.title("🏏 Cricket Player Registration")
st.write("Please enter your details and select your cricket role.")

st.divider()

# Create Cricket Form
with st.form("cricket"):

    # Personal details
    st.subheader("Personal Details")

    username = st.text_input("Username", placeholder="Enter username")

    email = st.text_input("Email", placeholder="example@gmail.com")

    phone = st.text_input("Phone Number", placeholder="Enter phone number")

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name", placeholder="Enter first name")

    with col2:
        last_name = st.text_input("Last Name", placeholder="Enter last name")

    st.divider()

    # Cricket player role
    st.subheader("Cricket Player Role")

    bowler = st.checkbox("Bowler")

    batsman = st.checkbox("Batsman")

    allrounder = st.checkbox("All-Rounder")

    # Submit button
    submitted = st.form_submit_button(
        "Register",
        use_container_width=True
    )

# Process form submission
if submitted:

    # Validate required fields
    if not all([
        username.strip(),
        email.strip(),
        phone.strip(),
        first_name.strip(),
        last_name.strip()
    ]):
        st.error("Please fill in all personal details.")

    # Validate email
    elif not re.fullmatch(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        email.strip()
    ):
        st.error("Please enter a valid email address.")

    # Validate phone number
    elif not re.fullmatch(r"\+?[0-9]{10,15}", phone.strip()):
        st.error("Please enter a valid phone number (10-15 digits).")

    # Validate cricket role
    elif not (bowler or batsman or allrounder):
        st.error("Please select at least one cricket role.")

    # Display registration details
    else:
        st.success("Cricket Registration Successful!")

        st.subheader("Registered Player Details")

        st.write(f"**Username:** {username}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone Number:** {phone}")
        st.write(f"**First Name:** {first_name}")
        st.write(f"**Last Name:** {last_name}")

        # Display selected roles
        st.subheader("Selected Cricket Roles")

        if bowler:
            st.write("🏏 Bowler")

        if batsman:
            st.write("🏏 Batsman")

        if allrounder:
            st.write("🏏 All-Rounder")

        st.info("Your cricket registration has been completed.")