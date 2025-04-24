from config import server
import requests, streamlit as st


def home(email):
    st.title("Home")
    st.success(f"Hello {email}")

    if st.button("logout"):
        requests.get(f"{server}/sign_out")
        st.success("bye")
        st.session_state.user_email = None
        st.rerun()


def auth():
    st.title("Authentication")
    option = st.selectbox("Choose:", options=["sign up", "login"])
    email = st.text_input("email")
    password = st.text_input("password", type="password")

    if option == "sign up" and st.button("sign up"):
        response = requests.post(f"{server}/sign_up", json=dict(email=email, password=password))
        data = response.json()
        if data and data["user"]:
            st.success("please confirm your email and log in")

    if option == "login" and st.button("login"):
        response = requests.post(f"{server}/sign_in", json=dict(email=email, password=password))
        data = response.json()
        if data and data["user"] and data["session"]:
            st.session_state.user_email = data["user"]["email"]
            st.success("welcome back")
            st.rerun()


if "user_email" not in st.session_state:
    st.session_state.user_email = None

if st.session_state.user_email:
    home(st.session_state.user_email)
else:
    auth()
