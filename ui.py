import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Cauditor", page_icon="🚀")

# Header Section
st.title("Cauditor")
st.write("Cauditor makes maintaining top-notch code quality a breeze! Cauditor ensures your code is optimized, secure, and efficient before it hits production. 🚀")

# File Upload Section
st.subheader("Upload Your File")
uploaded_file = st.file_uploader("Choose a file to upload", type=["py", "txt", "zip", "java", "js", "html"])

# Option to paste text
text_input = st.text_area("Or paste your code here...", height=200)

# Process File or Text Section
if uploaded_file:
    # Display the file name
    st.write(f"File Uploaded: {uploaded_file.name}")
    process_button = st.button("Process File")

    if process_button:
        # Create a form data object using the file uploaded
        files = {"file": uploaded_file.getvalue()}

        # Send the file to the backend (your API endpoint)
        response = requests.post("http://localhost:5000/analyze", files=files)

        if response.status_code == 200:
            st.success("File processed successfully!")
            st.json(response.json())  # Display the response from the backend
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

elif text_input:
    process_button = st.button("Process Text")

    if process_button:
        # Send the text to the backend (your API endpoint)
        response = requests.post("http://localhost:5000/analyze", data={"text": text_input})

        if response.status_code == 200:
            st.success("Text processed successfully!")
            st.json(response.json())  # Display the response from the backend
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
