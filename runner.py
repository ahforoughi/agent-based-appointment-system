# run main.py python file  
# python program to run main.py

import os
import subprocess
import sys


def run_main():
	# run main.py
	# subprocess.run(["python", "main.py", "--register"])
	# subprocess.run(["python", "main.py", "--login"])
	subprocess.run(["python", "main.py", "--get_appoinments_times"])

if __name__ == "__main__":
	run_main()
