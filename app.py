import streamlit as st

st.title('Welcome to Cat Kibble Box -CKB')

status = st.header('What would you like to do? ')
hobby = st.selectbox("Kibble-Box: ",
                     ['Box001', 'Box002', 'Box003'])

st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Options available: ",
                         ['Camera', 'Email', 'Eat'])

st.write("You selected", len(hobbies), 'options')


if st.button('Submit'):
    webbrowser.open("https://www.marca.com")
    st.success("Successful operation!!!!!")
