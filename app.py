import streamlit as st

# [theme]
# primaryColor="#29B969"
# base = 'light'
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#31333F"
# font="sans serif"

# st.session_state.logged_in = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "reports" not in st.session_state:
    st.session_state.reports = []

if "personality" not in st.session_state:
    st.session_state.personality = {}

if "language" not in st.session_state:
    st.session_state.language = "English"

def logoutt():
    # if st.button("Log out"):
    st.session_state.logged_in = False
    st.rerun()

st.logo("images/Logo.png")

# Pages
login = st.Page(r"login.py", title="Login", icon=":material/login:")
signup = st.Page(r"signup.py", title="Signup", icon=":material/assignment:")
logout = st.Page(logoutt, title="Logout", icon=":material/logout:")
intro = st.Page("intro.py", title="Home", icon=":material/home:")

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
chat = st.Page("Chatbot/chatbot.py", title="Chatbot", icon=":material/smart_toy:")
scan = st.Page("Scan/scan.py", title="Scan", icon=":material/radiology:")
ecg = st.Page("ECG/ecg.py", title="ECG Scan", icon=":material/ecg_heart:")
mbti = st.Page("MBTI/mbti.py", title="MBTI", icon=":material/psychology:")
profile = st.Page("profile.py", title="Profile", icon=":material/person:")
history = st.Page(r"diseasesHistory.py", title="Reports", icon=":material/view_list:")
edit = st.Page(r"edit.py", title="Edit", icon=":material/edit:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
# edit_basic = st.Page("edit_basic_info.py", title="Edit Name", icon=":material/edit:")
# edit_pass = st.Page("edit_password.py", title="Change Password", icon=":material/password:")
# app3 = st.Page("app3.py", icon=":material/logout:")

pages2 = {
    "":[login, signup, intro]
}

pages = {
    "": [profile, home],
    "Diagnosis": [chat, scan, ecg, mbti],
    "Settings": [history, settings, edit, logout]
}

# out = st.sidebar.button("Logout", use_container_width=1)
if st.session_state.logged_in == True:
    pg = st.navigation(pages)
    pg.run()
else:
    pg2 = st.navigation(pages2)
    pg2.run()