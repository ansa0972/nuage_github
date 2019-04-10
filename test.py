''' I have created this test environment using my own modules .This takes an argument from the user and checks if the argument provided by the user has entered an yaml extension. If yes then it proceeds to the test environments else it breaks the flow '''

import subprocess
import os
import argparse
import sys
import project_new
import shutil

''' This is the first test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir3 and dir4 and 4a. My expected output should combine files in dir3 and dir4 '''
def test_env1(file_name):

# Creating directories
	os.makedirs('dir_test1')
	os.makedirs('dir_test1/dir_test2')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4a')
	print("Successfully created the directories that will be used in the test")
	print("Creating the YAML files now")

# Creating YAML files

	with open("dir_test1/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	with open("dir_test1/dir_test2/dir_test3/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: red\nnames: ['lizard']\ntodo:\n  - vaccum:\n      - priority: high")
	with open("dir_test1/dir_test2/dir_test3/dir_test4/"+file_name, 'w') as fh:
		fh.write("size: 5\ncolor: blue\ncount: 7.5\nnames: ['cat','dog']\ntodo:\n  - laundry:\n      - priority: low")
	with open("dir_test1/dir_test2/dir_test3/dir_test4a/"+file_name, 'w') as fh:
		fh.write("size: 10\ncolor: purple")
	print("YAML files created")
	print("Passing the files in the source code")
	project_new.path_to_direc(file_name)
	shutil.rmtree('dir_test1')
	print("***********************Test Case 1 Passed*******************************************")

''' This is the second test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir2,dir3 , dir4 and dir4a. My expected output should combine files in all the directories'''

def test_env2(file_name):

# Creating Directories
	os.makedirs('dir_test1')
	os.makedirs('dir_test1/dir_test2')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4a')
	print("Successfully created the directories that will be used in the test")
	print("Creating the YAML files now")

# Creating YAML fies
	with open("dir_test1/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	with open("dir_test1/dir_test2/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: red\nnames: ['lion']\ntodo:\n  - dish-washing :\n      - priority: high")
	with open("dir_test1/dir_test2/dir_test3/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: red\nnames: ['lizard']\ntodo:\n  - vaccum:\n      - priority: high")
	with open("dir_test1/dir_test2/dir_test3/dir_test4/"+file_name, 'w') as fh:
		fh.write("size: 5\ncolor: blue\ncount: 7.5\nnames: ['cat','dog']\ntodo:\n  - laundry:\n      - priority: low")
	with open("dir_test1/dir_test2/dir_test3/dir_test4a/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	print("YAML files created")
	print("Passing the files in the source code")
	project_new.path_to_direc(file_name)
	shutil.rmtree('dir_test1')
	print("***********************Test Case 2 Passed*******************************************")

''' This is the third test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1  and dir4, dir4a. My expected output should show that the files should'nt merge each other '''

def test_env3(file_name):

# Creating Directories
	os.makedirs('dir_test1')
	os.makedirs('dir_test1/dir_test2')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4a')
	print("Successfully created the directories that will be used in the test")
	print("Creating the YAML files now")

# Creating YAML Files
	with open("dir_test1/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	with open("dir_test1/dir_test2/dir_test3/dir_test4/"+file_name, 'w') as fh:
		fh.write("size: 5\ncolor: blue\ncount: 7.5\nnames: ['cat','dog']\ntodo:\n  - laundry:\n      - priority: low")
	with open("dir_test1/dir_test2/dir_test3/dir_test4a/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	print("YAML files created")
	print("Passing the files in the source code")
	project_new.path_to_direc(file_name)
	shutil.rmtree('dir_test1')
	print("***********************Test Case 3 Passed*******************************************")

''' This is the fourth test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir2 and dir4,dir4a. My expected output should show files dont merge'''

def test_env4(file_name):

# Creating Directories
	os.makedirs('dir_test1')
	os.makedirs('dir_test1/dir_test2')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4')
	os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4a')
	print("Successfully created the directories that will be used in the test")
	print("Creating the YAML files now")

# Creating YAML files
	with open("dir_test1/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	with open("dir_test1/dir_test2/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: red\nnames: ['lion']\ntodo:\n  - dish-washing :\n      - priority: high")
	with open("dir_test1/dir_test2/dir_test3/dir_test4/"+file_name, 'w') as fh:
		fh.write("size: 5\ncolor: blue\ncount: 7.5\nnames: ['cat','dog']\ntodo:\n  - laundry:\n      - priority: low")
	with open("dir_test1/dir_test2/dir_test3/dir_test4a/"+file_name, 'w') as fh:
		fh.write("size: 2\ncolor: blue")
	print("YAML files created")
	print("Passing the files in the source code")
	project_new.path_to_direc(file_name)
	shutil.rmtree('dir_test1')
	print("***********************Test Case 4 Passed*******************************************")

# This function checks if the file name has proper extension
def check_filename(file_name):
	fh,extn= file_name.split('.')
	if extn=='yaml' or extn=='yml':
		return 1
	else:
		return 0
# Main Function 
if __name__=="__main__":
	parser=argparse.ArgumentParser()
	if len(sys.argv)==1:
		print("Error: Some parameters like filename are missing Please Check")
		sys.exit()
	parser.add_argument('file_name', help="Enter the yaml file-name location to test merging")
	args=parser.parse_args()
	file_name=args.file_name
	check=check_filename(file_name)
	if check==0:
		print("Error: You have entered the wrong extension")
	else:
		print("File extension is correct and creating the sample test environments")
		test_env1(file_name)
		test_env2(file_name)
		test_env3(file_name)
		test_env4(file_name)

