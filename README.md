# 🌍 Volunteer Registration Platform – Apex Community Foundation Ghana

This is a dynamic web application built with [Streamlit](https://streamlit.io) to collect volunteer applications from individuals interested in supporting community projects in Ghana.  

Developed by **Apex Community Foundation Ghana**  
In collaboration with **Impact Horizon UK** and **La Casa Maite**.

---

## 🚀 Features

- 🌐 Responsive landing page styled with Ghanaian flag colors
- 📋 User-friendly volunteer form with required validation
- 🌍 Dropdown for all countries using `pycountry`
- ✅ Auto-saves responses securely to a Google Sheet
- 📍 Integrated with Google Maps for location reference
- 🔐 Uses Streamlit Secrets for credential management

---

## 📦 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Data Storage**: Google Sheets (via `gspread`)
- **Auth**: Google Cloud Service Account (JSON key managed via `secrets.toml`)

---

## 📝 How to Use

### 1. Clone this Repository
```bash
git clone https://github.com/your-username/volunteer-form-app.git
cd volunteer-form-app
