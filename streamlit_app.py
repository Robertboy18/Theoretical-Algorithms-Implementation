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
        python_files = [file.replace("_", " ").replace(".py", "") for file in os.listdir(path) if file.endswith(".py")]
        return python_files
    else:
        return []


# Define function to clean up chapter titles
def chapter_title(chapter_folder):
    # Extract the chapter number and name
    chapter_index, chapter_name = chapter_folder.split("-", 1)
    # Remove leading/trailing whitespace and underscores
    chapter_name = chapter_name.strip().replace("_", " ")
    chapter_name = ''.join(filter(str.isalpha, chapter_name))
    # Capitalize the chapter name
    chapter_name = ' '.join(word.capitalize() for word in chapter_name.split())
    # Return the formatted chapter title
    return f"{chapter_name}"

# Display title
st.title("CLRS (Introduction to Algorithms) - Python/C++/Java Implementation")

# Display list of chapters
st.header("Chapters")
chapters = get_chapters()
chapter_index = st.selectbox("Select a chapter:", chapters)

# Display list of Python files in selected chapter
chapter_title = chapter_title(chapter_index)
st.header(f"Algorithms in {chapter_title}")
python_files = get_python_files(chapter_index)
if len(python_files) == 0:
    st.write("No Python files found.")
else:
    file_index = st.selectbox("Select a Python file:", python_files)

    # Display contents of selected Python file
    st.header(f"{file_index[20:]}")
    with open(os.path.join(file_index)) as f:
        st.code(f.read())
