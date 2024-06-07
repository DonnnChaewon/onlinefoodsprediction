import streamlit as st

st.write("Online Foods Prediction")
st.write("-------------------------------------")

name = st.text_input("Enter your name:\n")

while True:
  try:
    age = int(st.text_input("Enter your age:\n"))
    break
  except ValueError:
    st.error("Please enter a valid age (numbers only).")

gender = st.radio("Choose your gender", ("Male", "Female"))

marital_status = st.radio("Choose your marital status", ("Single", "Married", "Prefer not to say"))

occupation = st.radio("Choose your occupation", ("Student", "House wife", "Employee", "Self Employeed"))

monthly_income = st.text_input("Enter your monthly income:\n")

education = st.radio("Choose your education", ("Uneducated", "School", "Graduate", "Post Graduate", "Ph.D"))

while True:
  try:
    family_size = int(st.text_input("Enter your family size (how many members in your family):\n"))
    break
  except ValueError:
    st.error("Please enter a valid family size (numbers only).")

while True:
  try:
    latitude = float(st.text_input("Enter your location's latitude:\n"))
    break
  except ValueError:
    st.error("Please enter a valid latitude (in decimal, can be negative) (use . not ,).")

while True:
  try:
    longitude = float(st.text_input("Enter your location's longitude:\n"))
    break
  except ValueError:
    st.error("Please enter a valid longitude (in decimal, can be negative) (use . not ,).")


while True:
  try:
    pin_code = int(st.text_input("Enter your pin code:\n"))
    break
  except ValueError:
    st.error("Please enter a valid pin code (numbers only).")

feedback = st.radio("What is your feedback?", ("Positive", "Negative"))

buy_again = st.radio("Do you want to buy again?", ("Yes", "No"))

st.write(f"Name: {name}")
st.write(f"Age: {age}")
st.write(f"Gender: {gender}")
st.write(f"Marital Status: {marital_status}")
st.write(f"Occupation: {occupation}")
st.write(f"Monthly Income: {monthly_income}")
st.write(f"Education: {education}")
st.write(f"Family Size: {family_size}")
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")
st.write(f"Pin Code: {pin_code}")
st.write(f"Your Feedback: {feedback}")
st.write(f"Buy Again? {buy_again}")

if((feedback == "Positive") and (buy_again == "Yes")):
  st.write(f"User {name} wants to buy the same food again (or possibly a different food) for the next time.")
elif((feedback == "Negative") and (buy_again == "Yes")):
  st.write(f"User {name} don't want to buy the same food for the next time, unless with certain exceptions.")
elif((feedback == "Positive") and (buy_again == "No")):
  st.write(f"User {name} wants to buy a different food for the next time.")
elif((feedback == "Negative") and (buy_again == "No")):
  st.write(f"User {name} definitely don't want to buy the same food forever.")

# streamlit run onlinefoodsprediction.py [-- script args]