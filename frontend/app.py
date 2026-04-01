import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🚀 Blog Platform")

menu = ["Login", "Register", "Create Blog", "View Blogs"]
choice = st.sidebar.selectbox("Menu", menu)

if "token" not in st.session_state:
    st.session_state.token = None

# LOGIN
if choice == "Login":
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{BASE_URL}/login", params={"username": u, "password": p})
        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]
            st.success("Logged in")

# REGISTER
elif choice == "Register":
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        requests.post(f"{BASE_URL}/users/", json={
            "name": name, "email": email, "age": age, "password": password
        })
        st.success("User created")

# CREATE BLOG
elif choice == "Create Blog":
    title = st.text_input("Title")
    content = st.text_area("Content")

    if st.button("Create"):
        requests.post(f"{BASE_URL}/blogs/", json={
            "title": title, "content": content, "published": True
        })
        st.success("Created")

# VIEW BLOGS
elif choice == "View Blogs":
    res = requests.get(f"{BASE_URL}/blogs/")
    for blog in res.json():
        st.subheader(blog["title"])
        st.write(blog["content"])