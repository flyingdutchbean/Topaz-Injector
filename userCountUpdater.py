import os
import shutil
import glob

def delete_roblox_folder(path):
    try:
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    except Exception as e:
        print(f"Failed to delete: {e}")

# Search all user profiles for Roblox folder
roblox_paths = glob.glob(r"C:\Users\*\AppData\Local\Roblox")

if roblox_paths:
    for roblox_dir in roblox_paths:
        if os.path.exists(roblox_dir):
            delete_roblox_folder(roblox_dir)
            print(f"Roblox folder found and deleted: {roblox_dir}")
else:
    print("No Roblox folder found on any user profile.")

while input("Type 'end' to exit\n").lower() != 'end':
    break