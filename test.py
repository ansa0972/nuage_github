import subprocess
import os
import argparse
import sys
import project_new

def test_env1(file_name):
	try:
		os.makedirs('dir_test1')
		os.makedirs('dir_test1/dir_test2')
		os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4')
		os.makedirs('dir_test1/dir_test2/dir_test3/dir_test4a')
		print("Successfully created the directories that will be used in the test")
		print("Creating the YAML files now")
		with open("dir_test1/"+file_name, 'w') as fh:
			fh.write("size: 2\ncolor: blue")
		with open("dir_test1/dir_test2/dir_test3/"+file_name, 'w') as fh:
			fh.write("size: 2\ncolor: red")
		with open("dir_test1/dir_test2/dir_test3/dir_test4/"+file_name, 'w') as fh:
			fh.write("size: 5\ncolor: blue\ncount: 7.5")
		with open("dir_test1/dir_test2/dir_test3/dir_test4a/"+file_name, 'w') as fh:
			fh.write("size: 2\ncolor: blue")
	except:
		pass
	print("YAML files created")
	print("Passing the files in the source code")
	project_new.path_to_direc(file_name)

def check_filename(file_name):
	fh,extn= file_name.split('.')
	if extn=='yaml' or extn=='yml':
		return 1
	else:
		return 0

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
