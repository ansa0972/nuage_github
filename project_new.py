''' This is the main source code. This performs the function of merging the different YAML files based on the fact that : String Int and Float should merge in a way that the child directory should overlap the parent directory and if some extra terms are present in the parent directory it should also merge, if a common list present in both parent as well as child directory, then it should concat the list of child with the parent directory. if nested loops are present then it should preserve the key words while merging. Here the merging happens in the following condition : suppose dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 are directories created and we have input yaml files in the directories dir1 dir3 and dir4 then yaml files of dir3 and dir4 should merge and yaml file of dir1 should be ignored as dir2 doesn't have an input yaml file''' 

import os
import yaml
import copy
import sys

# This function does the merging part of the files
def recursive_copy(target,src):
	for k, v in src.items():
		if type(v) == list:
			if not k in target:
				target[k] = copy.deepcopy(v)
			else:
				target[k].extend(v)
		elif type(v) == dict:
			if not k in target:
				target[k] = copy.deepcopy(v)
			else:
				recursive_copy(target[k], v)
		elif type(v) == set:
			if not k in target:
				target[k] = v.copy()
			else:
				target[k].update(v.copy())
		else:
			target[k] = copy.copy(v)

# This function is responsible for printing the dictionary returned in YAML format
def yaml_op(consecutive_path,file_name):
	for i in range(0,len(consecutive_path)):
		if i == len(consecutive_path)-1:
			break
		if i == 0:
			with open(consecutive_path[i]+'/'+file_name) as fp:
				data = yaml.load(fp)
		else:
			data=data_1
		with open(consecutive_path[i+1]+'/'+file_name) as fp:
			data_1 = yaml.load(fp)
		recursive_copy(data_1,data)
	print("Files After Merging")
	print(yaml.dump(data_1,default_flow_style=False))

# This function checks for consecutive paths and ignores if not consecutive paths
def consec_path(path_to_dir,file_name):
	consecutive_path=[]
	j=0
	for i in range (0, len(path_to_dir)):
		if i ==  len(path_to_dir)-1:
			if len(path_to_dir[i].split('/'))+1==len(path_to_dir[i-1].split('/')):
				consecutive_path.append(path_to_dir[i])
				break
			break
		else:
			if len(path_to_dir[i+1].split('/'))+1==len(path_to_dir[i].split('/')):
				if j == 1:
					consecutive_path.append(path_to_dir[i+1])
				else:
					consecutive_path.append(path_to_dir[i])
					consecutive_path.append(path_to_dir[i+1])
					j=1
			else:
				break
	if len(consecutive_path) >1:
		yaml_op(consecutive_path,file_name)
	else:
		print("There are no consecutive files to merge")

# This function takes the input from the test environment and then separates then ignores sister directories and creates a list of consecutive directories
def path_to_direc(file_name):
	path_to_dir=[]
	l=0
	for root, dirs, files in os.walk("."):
		for file in files:
			if file == file_name:
				if len(root.split('/')) != l:
					path_to_dir.append(root)
					l=len(root.split('/')) 
	path_to_dir.reverse()
	consec_path(path_to_dir,file_name)
