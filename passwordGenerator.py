import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    length = min(len(password) / 12, 1) 
    digit = any(char.isdigit() for char in password)
    special_char = any(char in string.punctuation for char in password)
    
    strength = length + digit + special_char

    if strength >= 2.5:
        return "Strong", "green"
    elif strength >= 1.5:
        return "Medium", "orange"
    else:
        return "Weak", "red"

st.title("Password Generator & Strength Checker")

st.header("Customize Your Password")
password_length = st.slider("Password Length", 6, 32, 12)
use_digits = st.checkbox("Include Numbers", True)
use_special_chars = st.checkbox("Include Special Characters", True)

if st.button("Generate Password"):
    password = generate_password(password_length, use_digits, use_special_chars)
    strength, color = password_strength(password)
    st.success(f"**Generated Password:** `{password}`")
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
else:
    st.warning("Click 'Generate Password' to create a password.")

