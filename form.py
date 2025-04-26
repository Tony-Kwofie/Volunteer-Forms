import streamlit as st
import pandas as pd
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import pycountry

# Tool: Format raw private key with correct \n for secrets.toml


def format_private_key(raw_key):
    lines = raw_key.strip().splitlines()
    return "\\n".join(lines)


# Setup Google Sheets
SHEET_NAME = "Volunteer Form Responses"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
# ✅ FIX: Load credentials from Streamlit secrets (not from file)
credentials = json.loads(st.secrets["gcp_service_account"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# Page config
st.set_page_config(page_title="Volunteer in Ghana", layout="wide")

# --- BANNER ---
st.markdown(
    """
    <div style='background: linear-gradient(to right, #e30b17, #fcd116, #007847); padding: 60px 30px; text-align: center; color: white; border-radius: 8px;'>
        <h1 style='font-size: 50px;'>🌍 Join Us in Ghana</h1>
        <p style='font-size: 22px;'>Make a difference. Empower communities. Experience cultural exchange.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- INTRO SECTION ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 40px;'>
        <h2 style='color: #e30b17;'>Apex Community Foundation Ghana</h2>
        <p style='font-size: 18px;'>In collaboration with <strong>Impact Horizon UK</strong> and <strong>La Casa Maite</strong></p>
        <p style='font-size: 16px; color: #333;'>
            📞 UK: +44 7309 818448 &nbsp;&nbsp;|&nbsp;&nbsp; Europe: +34 646 644 212 <br>
            📱 Ghana (WhatsApp): +233 548 233 950 <br>
            📍 <a href="https://maps.app.goo.gl/LwGa65LXxzZz39JR8" target="_blank">View Location on Google Maps</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- FORM ---
st.markdown("<hr style='border:1px solid #eee;'>", unsafe_allow_html=True)
st.header("📝 Volunteer Registration Form")
st.markdown(
    "<p style='color:#444;'>All fields are required.</p>", unsafe_allow_html=True
)

# List of countries
countries = sorted([country.name for country in pycountry.countries])

with st.form("volunteer_form", clear_on_submit=True):
    st.subheader("✅ Basic Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    dob = st.date_input(
        "Date of Birth", min_value=date(1850, 1, 1), max_value=date.today()
    )
    nationality = st.selectbox("Country of Residence / Nationality", countries)

    st.subheader("🛂 Travel & Availability")
    start_date = st.date_input("Preferred Start Date", min_value=date.today())
    traveled = st.radio("Have you traveled to Ghana before?", ["Yes", "No"])
    passport = st.radio("Do you have a valid passport?", ["Yes", "No"])
    expenses = st.radio(
        "Are you able to cover your own travel expenses?", ["Yes", "No"]
    )

    st.subheader("🎓 Background & Skills")
    education = st.text_input("Educational Background")
    occupation = st.text_input("Current Occupation")
    skills = st.text_area("Relevant Skills or Experience")
    languages = st.text_input("Languages Spoken")

    st.subheader("💬 Motivation & Interests")
    motivation = st.text_area("Why do you want to volunteer with us?")
    interest = st.text_input("What kind of volunteer work are you most interested in?")
    past_experience = st.text_area(
        "Have you volunteered before? Where and in what capacity?"
    )

    submitted = st.form_submit_button("Submit")

    if submitted:
        required = [
            full_name,
            email,
            phone,
            nationality,
            education,
            occupation,
            skills,
            languages,
            motivation,
            interest,
        ]
        if not all(required):
            st.error("❌ Please complete all required fields before submitting.")
        else:
            new_row = [
                full_name,
                email,
                phone,
                str(dob),
                nationality,
                str(start_date),
                traveled,
                passport,
                expenses,
                education,
                occupation,
                skills,
                languages,
                motivation,
                interest,
                past_experience,
                str(pd.Timestamp.now()),
            ]
            try:
                sheet.append_row(new_row)
                st.success(
                    "✅ Your application has been submitted and saved to Google Sheets!"
                )
            except Exception as e:
                st.error(f"❌ Error submitting to Google Sheets: {e}")

# --- FOOTER ---
st.markdown(
    """
    <hr style='margin-top: 50px; border: none; border-top: 1px solid #ccc;'>
    <div style='text-align: center; font-size: 14px; color: #888; padding: 20px;'>
        © 2025 Apex Community Foundation Ghana • Designed with ❤️ in collaboration with Impact Horizon UK & La Casa Maite
    </div>
    """,
    unsafe_allow_html=True,
)
