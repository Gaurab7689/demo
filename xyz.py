import streamlit as st
name=st.text_input("Enter Your Name")
fathername=st.text_input("Enter Your Father Name")
mothername=st.text_input("Enter Your Mother Name")
age=st.text_input("Enter Your Age")
gender=st.text_input("Enter Your Gender")
Birth_year=st.text_input("Enter Your Birth Year")
Info=st.selectbox("Hobbies:",['Dancing','Singing','Writing'])
button=st.button("Click Me")
if button:
    st.markdown(f"""
    Name: {name}\n
    FatherName: {fathername}\n
    MotherName: {mothername}\n
    Age:{age}\n
    Gender:{gender}\n
    Year:{Birth_year}\n
    Info: {Info}
    """)
