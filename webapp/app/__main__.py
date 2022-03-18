import streamlit as st
# import webbrowser

st.title("Welcome to Cat Kibble Box -CKB")

status = st.header("What would you like to do? ")
kibblepi = st.selectbox("Kibble-Box: ", ["Box001", "Box002", "Box003"])

st.write("Your Kibble-box  is: ", kibblepi)

options = st.multiselect("Options available: ", ["Camera", "Email", "Eat"])

st.write("You selected", len(options), "options")


# if st.button("Submit"):
#     webbrowser.open("https://www.marca.com")
#     st.success("Successful operation!!!!!")


st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/">
        <button>
            RaspberryPi - Home
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/send-email">
        <button>
            Send Email
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/push-button">
        <button>
            Push-Button
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/servo-kibblepi">
        <button>
            Servo-Motor
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)

st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/led/17/state/1">
        <button>
            LED 17 ON
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    <a target="_self" href="http://devrulls.ddns.net:8080/led/17/state/0">
        <button>
            LED 17 OFF
        </button>
    </a>
    """,
    unsafe_allow_html=True,
)
