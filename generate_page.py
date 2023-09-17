import os
import sys


root_path=sys.argv[1]

def generate_html_listing(directory):
    output = ['<html><head><title>Directory Listing</title></head><body>']
    output.append('<h2>Directory Listing</h2>')

    def walk_directory(dir_path, depth=0):
        output = []
        indent = '  ' * depth
        output.append(f"{indent}<ul>")

        # List directories
        for name in sorted(os.listdir(dir_path)):
            full_path = os.path.join(dir_path, name)
            if os.path.isdir(full_path):
                output.append(f"{indent}  <li>{name}")
                output.extend(walk_directory(full_path, depth+1))
                output.append(f"{indent}  </li>")

        # List files
        for name in sorted(os.listdir(dir_path)):
            full_path = os.path.join(dir_path, name)
            rel_path = os.path.relpath(full_path, directory)
            if os.path.isfile(full_path):
                output.append(f"{indent}  <li><a href='{rel_path}'>{name}</a></li>")

        output.append(f"{indent}</ul>")
        return output

    output.extend(walk_directory(directory))
    output.append('</body></html>')

    return '\n'.join(output)

print(generate_html_listing(root_path))