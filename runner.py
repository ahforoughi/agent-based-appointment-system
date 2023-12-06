# run main.py python file  
# python program to run main.py
# and get the final line of output


import os
import subprocess
import sys


# run the process and store the output
def run_main():
	# run main.py
	# subprocess.run(["python", "main.py", "--register"])
	# subprocess.run(["python", "main.py", "--login"])
	
	# run main.py and get the final line of output
	output = subprocess.check_output(["python", "main.py", "--get_appoinments_times"])
	print(output.splitlines()[-1].decode("utf-8"))

if __name__ == "__main__":
	run_main()
