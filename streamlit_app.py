
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "Let's start building! For help, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
failures = st.number_input("Number of past class failures", min_value=0, max_value=4)
higher = st.selectbox('Wants to take higher education?', ('Yes', 'No'))
G1= st.slider("Your First Period Grade", 0, 20, 10)
G2= st.slider("Your Second Period Grade", 0, 20, 10)

st.button("Predict Final Grade")