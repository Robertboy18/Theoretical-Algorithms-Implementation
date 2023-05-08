import os
import streamlit as st

# Set page title
st.set_page_config(page_title="My Repository")

# Define function to get all chapter folders in repository
def get_chapters():
    return [folder for folder in os.listdir() if os.path.isdir(folder)]

# Define function to get all Python files in a folder
def get_python_files(folder):
    path = os.path.join(folder, "python")
    if os.path.exists(path):
        return [file for file in os.listdir(path) if file.endswith(".py")]
    else:
        return []

# Display title
st.title("Welcome to my Repository")

# Display list of chapters
st.header("Chapters")
chapters = get_chapters()
chapter_index = st.selectbox("Select a chapter:", chapters)

# Display list of Python files in selected chapter
st.header(f"Python files in {chapter_index}")
python_files = get_python_files(os.path.join(chapter_index, "python"))
if len(python_files) == 0:
    st.write("No Python files found.")
else:
    file_index = st.selectbox("Select a Python file:", python_files)

    # Display contents of selected Python file
    st.header(f"Contents of {file_index}")
    with open(os.path.join(chapter_index, "python", file_index)) as f:
        st.code(f.read())
