from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get a list of all files in the Projects folder
    project_folder = '/home/m/userInterface/Projects'
    file_names = os.listdir(project_folder)
    # Create an empty dictionary to store the file contents
    file_contents = {}
    # Loop through the file names and read their contents
    for file_name in file_names:
        # Open the file in read mode
        file_path = os.path.join(project_folder, file_name)
        with open(file_path, 'r') as file:
            # Read the file content and store it in the dictionary
            file_content = file.read()
            file_contents[file_name] = file_content
    # Return a template that displays the file names and contents
    return render_template('index.html', file_contents=file_contents)

if __name__ == "__main__":
    app.run(debug=True)