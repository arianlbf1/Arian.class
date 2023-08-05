import os 
import shutil 

folder_path = input("Please enter the path to your folder:")

try:
    shutil.rmtree(folder_path)
    print(f"Folder '{folder_path}' and its contents successfully deleted.")
except OSError as e:
    print(f"Error deleting the folder: {e}")
