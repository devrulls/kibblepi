import webbrowser

import streamlit as st

st.title("Welcome to Cat Kibble Box -CKB")

status = st.header("What would you like to do? ")
hobby = st.selectbox("Kibble-Box: ", ["Box001", "Box002", "Box003"])

st.write("Your Kibble-box  is: ", hobby)

options = st.multiselect("Options available: ", ["Camera", "Email", "Eat"])

st.write("You selected", len(hobby), "options")


if st.button("Submit"):
    webbrowser.open("https://www.marca.com")
    st.success("Successful operation!!!!!")


st.write(
    f"""
    <a target="_self" href="https://marca.com">
        <button>
            redirect via Marca
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
