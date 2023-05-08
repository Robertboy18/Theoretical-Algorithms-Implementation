import os
import streamlit as st

# Set page title
st.set_page_config(page_title="Introduction to Algorithms - Code Implementation")


# Define function to get all chapter folders in repository
def get_chapters():
    # Get all folders in current directory
    folders = os.listdir()

    # Extract the chapter number from the folder name
    def get_chapter_number(folder_name):
        return int(folder_name.split('-')[0])

    # Filter folders that start with a number and sort by chapter number
    filtered_folders = sorted([f for f in folders if f.startswith(tuple(map(str, range(10))))])
    sorted_folders = sorted(filtered_folders, key=get_chapter_number)

    return sorted_folders

# Define function to get all Python files in a folder
def get_python_files(folder):
    path = os.path.join(folder, "Python")
    if os.path.exists(path):
        return [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".py")]
    else:
        return []


# Display title
st.title("Introduction to Algorithms - Code Implementation")

# Display list of chapters
st.header("Chapters")
chapters = get_chapters()
chapter_index = st.selectbox("Select a chapter:", chapters)

# Display list of Python files in selected chapter
st.header(f"Algorithms in {chapter_index}")
python_files = get_python_files(chapter_index)
if len(python_files) == 0:
    st.write("No Python files found.")
else:
    file_index = st.selectbox("Select a Python file:", python_files)

    # Display contents of selected Python file
    st.header(f"Contents of {file_index}")
    with open(os.path.join(file_index)) as f:
        st.code(f.read())
