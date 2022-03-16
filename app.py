import streamlit as st

st.title("Welcome to Cat Kibble Box -CKB")

status = st.header("What would you like to do? ")
kibblepi = st.selectbox("Kibble-Box: ", ["Box001", "Box002", "Box003"])

st.write("Your Kibble-box  is: ", kibblepi)

options = st.multiselect("Options available: ", ["Camera", "Email", "Eat"])

st.write("You selected", len(options), "options")


