import streamlit as st
import pandas as pd 

# Title of Page 

st.title("Welcome to My Streamlit App")

# Add required fields notice
st.markdown("**Note:** All fields marked with * are required")

# Text Input 

name=st.text_input("Enter your name: *", placeholder="Required field")
age=st.number_input("Enter your Age: *", min_value=1, max_value=120, value=1)


uploaded_file=st.file_uploader("Upload a CSV file *", type=["csv"], help="This field is required")

if uploaded_file is not None:
    print(uploaded_file)
    df=pd.read_csv(uploaded_file)
    st.write(df)

if st.button("Submit"):

    with st.spinner("Processing..."):
        try:
            st.ballons()
        except Exception as e:
            print(e)
    # Check if all fields are filled
    if not name:
        st.error("Please enter your name.")
    elif age <= 0:
        st.error("Please enter a valid age.")
    elif uploaded_file is None:
        st.error("Please upload a CSV file.")
    else:
        st.success(f"Hello {name}, welcome to my Streamlit app!")
        st.write("Form submitted successfully with all required fields!")