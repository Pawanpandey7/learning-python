import os # imports the os module interacting with the file system
import shutil # imports shutil for moving files

#set the path of the folder you want to organize
folder_path = "sample"

#get a list of all files and folders in the given folder
items = os.listdir(folder_path)

#loop through each item in the folder
for item in items:
    item_path = os.path.join(folder_path, item)

    #check if its a file(not a folder)
    if os.path.isfile(item_path):
        #split the file name and the extension
        _, extension = os.path.splitext(item)

        #if there is no extension, skip the file
        if extension =="":
            continue

        #remove the dot from the extension
        extension = extension[1:]

        #create a new folder path based on the extension
        folder_by_extension = os.path.join(folder_path, extension)

        #if the folder for this extension doesnot exist, create it 
        if not os.path.exists(folder_by_extension):
            os.makedirs(folder_by_extension)

        #move th file to the corresponding extension folder
        shutil.move(item_path, os.path.join(folder_by_extension, item)) 
           





