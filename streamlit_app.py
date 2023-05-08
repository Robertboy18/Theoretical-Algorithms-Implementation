import os
import streamlit as st
import regex as re

# Set page title
st.set_page_config(page_title="Introduction to Algorithms - Code Implementation")


# Define function to get all chapter folders in repository
def get_chapters():
    # Get all folders in current directory
    folders = os.listdir()

    # Sort folders by chapter number
    chapter_regex = re.compile(r"^\d+-")
    sorted_folders = sorted([folder for folder in folders if chapter_regex.match(folder)])

    # Return only folders that start with a number
    return [folder for folder in sorted_folders if os.path.isdir(folder)]


# Define function to get all Python files in a folder
def get_python_files(folder):
    path = os.path.join(folder, "Python")
    if os.path.exists(path):
        return [file for file in os.listdir(path) if file.endswith(".py")]
    else:
        return []

# Display title
st.title("Introduction to Algorithms - Code Implementation")

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
