import os
import yaml
import copy
import sys

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

def yaml_op(consecutive_path,file_name):
	for i in range(0,len(consecutive_path)):
		if i == len(consecutive_path)-1:
			break
		with open(consecutive_path[i]+'/'+file_name) as fp:
			data = yaml.load(fp)
		with open(consecutive_path[i+1]+'/'+file_name) as fp:
			data_1 = yaml.load(fp)
		recursive_copy(data_1,data)
		print(yaml.dump(data_1,default_flow_style=False))

def consec_path(path_to_dir,file_name):
	consecutive_path= []
	j=0
	for i in range (0, len(path_to_dir)):
		if j==1:
			j=0
			continue
		if i ==  len(path_to_dir)-1:
			if len(path_to_dir[i].split('/'))==len(path_to_dir[i-1].split('/'))+1:
				consecutive_path.append(path_to_dir[i])
				break
			break
		else:
			if len(path_to_dir[i+1].split('/'))==len(path_to_dir[i].split('/'))+1:
				print(path_to_dir[i])
				consecutive_path.append(path_to_dir[i])
			if len(path_to_dir[i+1].split('/'))==len(path_to_dir[i].split('/')):
				consecutive_path.append(path_to_dir[i])
				j=1


	if len(consecutive_path) != 0:
		consecutive_path.reverse()
		print(consecutive_path)
		yaml_op(consecutive_path,file_name)
	else:
		print("There are no consecutive files to merge")
		sys.exit()

def path_to_direc(file_name):
	path_to_dir=[]
	for root, dirs, files in os.walk("."):
#		print(files)
		for file in files:
			if file == file_name:
				print(file)
				path_to_dir.append(root)
	print(path_to_dir)
	consec_path(path_to_dir,file_name)
