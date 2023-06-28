# Python file to list down all the files in the directory

import os

directory = "dist/downloaded_wheels"
index_file = "index.html"

file_list = os.list_dir(directory)

# Generate the HTML content
html_content = <html>\n<body>\n</html>

for file_name in file_list:
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        html_content += f"<a href='{file_path}' download>{file_path}</a><br>"

html_content += "</body>\n</html>"
