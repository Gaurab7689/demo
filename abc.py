import streamlit as st

name=st.text_input('Enter Your Name')
father_name=st.text_input('Enter Your Father Name')
mother_name=st.text_input('Enter Your Mother Name')
age=st.text_input('Enter Your Age')
gender=st.text_input('Enter Your Gender')
address=st.text_input('Enter Your Address')
city=st.text_input('Enter Your City')
Info=st.selectbox("Honnies:", ['Dancing','Learning','Singing'])
button=st.button('Click Me!')
if button :
    st.markdown(f""" 
    Name: {name}
    Father Name: {father_name}
    Mother Name: {mother_name}
    Age: {age}
    Gender: {gender}
    Address: {address}
    City: {city}
    Info: {Info}
    """)