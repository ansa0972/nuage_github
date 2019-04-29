<< Project by Animesh Kumar Sahu >> << Master of Science in CU Boulder >> 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The source code:
This is the main source code. This performs the function of merging the different YAML files based on the fact that : String Int and Float should merge in a way that the child directory should overlap the parent directory and if some extra terms are present in the parent directory it should also merge, if a common list present in both parent as well as child directory, then it should concat the list of child with the parent directory. if nested loops are present then it should preserve the key words while merging. Here the merging happens in the following condition : suppose dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 are directories created and we have input yaml files in the directories dir1 dir3 and dir4 then yaml files of dir3 and dir4 should merge and yaml file of dir1 should be ignored as dir2 doesn't have an input yaml file
The functions I used:

1. recursive_copy(): This function does the merging part of the files

2. yaml_op(): This function is responsible for printing the dictionary returned in YAML format

3. consec_path(): This function checks for consecutive paths and ignores if not consecutive paths

4. path_to_direc(): This function takes the input from the test environment and then separates then ignores sister directories and creates a list of consecutive directories

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The test code:
I have created this test environment using my own modules .This takes an argument from the user and checks if the argument provided by the user has entered an yaml extension. If yes then it proceeds to the test environments else it breaks the flow

1. test_env1(): This is the first test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir3 and dir4 and 4a. My expected output should combine files in dir3 and dir4 

2. test_env2(): This is the second test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir2,dir3 , dir4 and dir4a. My expected output should combine files in all the directories

3. test_env3(): This is the third test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1  and dir4, dir4a. My expected output should show that the files should'nt merge each other

4. test_env4(): This is the fourth test environment. Here I created the test directories dir1, dir1/dir2, dir1/dir2/dir3, dir1/dir2/dir3/dir4 and dir1/dir2/dir3/dir4a. After creating the directories I created the input.yaml files in the dir1, dir2 and dir4,dir4a. My expected output should show files dont merge
