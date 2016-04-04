__author__ = 'mkie006'
import os;
import sys;
import hashlib;
import os.path, time;
import json;

arguments = []
for arg in sys.argv:
    arguments.append(arg)

#Creates the relative paths for arguments one and two.
sourcepathArgOne = os.path.abspath(arguments[1])
sourcepathArgTwo = os.path.abspath(arguments[2])

# the below creates a time stamp for the particular file
# for file in os.listdir(dir_name):
#         file_list[file] = time.ctime(os.path.getmtime(sourcepathArgOne+"/"+file))

#For the sha-256 digest we must use a hash.hexdigest()
#This represents the hash in a hexadecimal string of type double length
#For the sync file you need a dictionary key with an associated list elements. These hold the data.
def check_Directories():
#Checks to see if the directories are valid
    #Assigns a boolean to identify valid directories
    directory_one = False
    directory_two = False

    #Checks to see if args one is valid
    if os.path.isdir(sourcepathArgOne):
        directory_one=True
    # print("argsone "+arguments[1])
    # print(directory_one)

    #Checks to see if args two is valid
    if os.path.isdir(sourcepathArgTwo):
        directory_two=True
    # print("args2 "+arguments[2])
    # print(directory_two)



    #Creates the directories, returns an error if neither directory is found.
    if directory_one==True and directory_two==False:
        os.mkdir(arguments[2])
    if directory_one==False and directory_two==True:
        os.mkdir(arguments[1])
    if directory_one==False and directory_two==False:
        sys.exit("This is not a valid directory")

    #Searches through the specified input directory and calls createSync if no sync file detected
def search_Directory(dir_name):
    #Creates a dictionary for the list of files and associated values
    file_list = {}
    directory_list = os.listdir(dir_name)
    # if directory_list.__len__()==0:
    #     print("there are no files in this directory")
    #     return file_list
    if ".sync" not in file_list:
        createSync(dir_name, file_list)
    return file_list

def createSync(dir_name, file_list):
    #Creates the file name sync and dictionary
    file_name = "/.sync"
    file_dictionary = {}
    file_list = os.listdir(dir_name)
    if ".sync" in file_list:
        file_list.remove(".sync")
    print("Directory name :"+dir_name)
    print(os.listdir(dir_name))

    #The directory name-dir_name in this case being the name of the folder
    #for each file in the listed directory "Hello", open the file, read, and then create an entry in the dictionary
    #The dictionary will then be outputted to the file.
    for file in file_list:
        hash = hashlib.sha256()
        with open(dir_name+"/"+file, "r") as afile:
            buffer = afile.read()
            hash.update(buffer)
        current_time = time.ctime(os.path.getmtime(sourcepathArgOne+"/"+file))
        current_timef = time.strptime(current_time, "%a %b %d %H:%M:%S %Y")
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S +1200 ")
        file_dictionary[file+".txt"] = [formatted_time, hash.hexdigest()]
    print(file_dictionary)
    f = open(dir_name+file_name, "a")
    f.write(json.dumps(file_dictionary))
    print("I have created a sync file")


check_Directories()
file_list = search_Directory(sourcepathArgOne)
second_file = search_Directory(sourcepathArgTwo)

# To synchronize we need to search through each dictionary again
#We could actually retrieve the file_dictionary and compare the results of each
#Then update if necessary.



