import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Display title
st.title("Welcome to my Streamlit App")

# Add text input box
user_input = st.text_input("Enter some text here:")

# Add button to submit text
if st.button("Submit"):
    # Display the text that was entered into the input box
    st.write(f"You entered: {user_input}")
