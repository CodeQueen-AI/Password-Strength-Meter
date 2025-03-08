import streamlit as st
import re
import random
import string

st.markdown("<h1 style='text-align: center;'>🔒 Password Strength Checker & Generator</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

def check_strength(password):
    length_criteria = len(password) >= 8
    lower_case = bool(re.search(r"[a-z]", password))
    upper_case = bool(re.search(r"[A-Z]", password))
    digit = bool(re.search(r"\d", password))
    special_char = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    strength = sum([length_criteria, lower_case, upper_case, digit, special_char])

    suggestions = []
    if not length_criteria:
        suggestions.append("🔹 Use at least 8 characters.")
    if not lower_case:
        suggestions.append("🔹 Add lowercase letters (a-z).")
    if not upper_case:
        suggestions.append("🔹 Add uppercase letters (A-Z).")
    if not digit:
        suggestions.append("🔹 Include numbers (0-9).")
    if not special_char:
        suggestions.append("🔹 Use special characters (!@#$%^&*).")

    if strength == 5:
        return "🟢 Strong", suggestions
    elif strength >= 3:
        return "🟡 Medium", suggestions
    else:
        return "🔴 Weak", suggestions

def generate_strong_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))  

if password:
    strength, suggestions = check_strength(password)
    st.markdown(f"<h3>Password Strength: {strength}</h3>", unsafe_allow_html=True)

    if suggestions:
        st.markdown("**💡 Suggestions to Improve Your Password:**")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

if st.button("✨ Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("💪 Strong Password: " + strong_password)






























