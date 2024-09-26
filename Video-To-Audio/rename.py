import os

# Function to rename all directories in a given parent directory
def fix_all_directory_names(parent_directory):
    # Loop through all items in the parent directory
    for item in os.listdir(parent_directory):
        item_path = os.path.join(parent_directory, item)
        
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Replace spaces with hyphens in the directory name
            new_directory_name = item.replace(" ", "-")
            new_directory_path = os.path.join(parent_directory, new_directory_name)
            
            # Rename the directory if needed
            if item_path != new_directory_path:
                os.rename(item_path, new_directory_path)
                print(f"Renamed: {item_path} -> {new_directory_path}")
            else:
                print(f"Directory '{item}' is already correctly formatted")

# Specify the parent directory containing the folders to rename
parent_directory_path = "/home/devops/python"  # Replace with the correct path

fix_all_directory_names(parent_directory_path)
