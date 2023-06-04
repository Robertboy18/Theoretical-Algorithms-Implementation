import os
import streamlit as st

# Set page title
st.set_page_config(page_title="Introduction to Algorithms - Code Implementation", layout="wide")

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
        python_files = [file.replace("_", " ").replace(".py", "") for file in os.listdir(path) if file.endswith(".py")]
        return [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".py")], python_files
    else:
        return []
    
# Define function to get all README files in a folder
def get_readme_files(folder):
    path = os.path.join(folder)
    if os.path.exists(path):
        readme_files = [file.replace("_", " ").replace(".md", "") for file in os.listdir(path) if file.endswith("Readme.md")]
        return [os.path.join(path, file) for file in os.listdir(path) if file.endswith("Readme.md")], readme_files
    else:
        return []


# Define function to clean up chapter titles
def chapter_title(chapter_folder):
    # Extract the chapter number and name
    chapter_index, chapter_name = chapter_folder.split("-", 1)
    # Remove leading/trailing whitespace and underscores
    chapter_name = chapter_name.strip().replace("_", " ")
    # Return the formatted chapter title
    return f"{chapter_name}"

# Display title
st.title("Introduction to Algorithms (CLRS) - Code Implementation")

# Define repository details section
st.write("## Repository Details")
st.write("This repository is organized by chapter, with each chapter containing its corresponding algorithms. Each algorithm is accompanied by a detailed explanation and analysis of its time and space complexities.")
st.write(f"Check out the source code and how to contribute at [GitHub](https://github.com/Robertboy18/Theoretical-Algorithms-Implementation).")
st.write("---")  # Add a horizontal line to separate the repository details from the rest of the app

# Display list of chapters
st.header("Chapters")
chapters = get_chapters()
chapter_index = st.selectbox("Select a chapter:", chapters)

chapter_title = chapter_title(chapter_index)
# Display read me
st.header(f"Outline of {chapter_title}")
original_files, readme_files = get_readme_files(chapter_index)
if len(readme_files) == 0:
    st.write("No Chapter Outline found.")
else:
    # Display contents of selected README file
    with open(original_files[0], "r", encoding="utf-8") as f:
        st.markdown(f.read())

# Display list of Python files in selected chapter
st.header(f"Algorithms in {chapter_title}")
original_files, python_files = get_python_files(chapter_index)
if len(python_files) == 0:
    st.write("No Python files found.")
else:
    file_index = st.selectbox("Select a Python file:", original_files)

    # Display contents of selected Python file
    with open(os.path.join(file_index)) as f:
        st.code(f.read())


# Contributers
st.header("Contributers")
st.write("This repository is maintained by [Robert Joseph George](https://github.com/Robertboy18)")