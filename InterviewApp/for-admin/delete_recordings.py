import os

def delete_recordings(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an interview transcript
        if filename.startswith("Interview_") and filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

# Example usage:
delete_recordings("../recordings")  # Replace with your folder path where files are saved
