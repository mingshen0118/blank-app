
import streamlit as st

st.title("Predict Your Final Grade 💯")
st.write(
    "Please provide the following information!"
)
failures = st.number_input("Number of Past Class Failures", min_value=0, max_value=4)
higher = st.selectbox('Want To Take Higher Education?', ('Yes', 'No'))
G1= st.slider("Your First Period Grade", 0, 20, 10)
G2= st.slider("Your Second Period Grade", 0, 20, 10)

if st.button("Predict Final Grade"):
    average = (G1 + G2) / 2
    st.write(f"Congratulations! 🎉 Your Predicted Final Grade is: {average}")