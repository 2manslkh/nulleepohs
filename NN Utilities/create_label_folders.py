# -*- coding: utf-8 -*-
"""
create_data_folders()
[Can be run either standalone or as a module!]

@author: methylDragon

                                   .     .
                                .  |\-^-/|  .
                               /| } O.=.O { |\
                              /´ \ \_ ~ _/ / `\
                            /´ |  \-/ ~ \-/  | `\
                            |   |  /\\ //\  |   |
                             \|\|\/-""-""-\/|/|/
                                     ______/ /
                                     '------'
                       _   _        _  ___
             _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _
            | '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \
            |_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                               |__/                 |___/
            -------------------------------------------------------
                           github.com/methylDragon

Description:
This importable module defines a function that sifts through a folder of
labelled data, and copy-sorts them into subfolders.

This will create new folders and fill them with copies of files!!

Functions:
- create_label_folders(data_folder)

Note:
Ensure your parent folders are placed in the same folder as your script

Structure your files and folder as such:
    Root directory:
        - your_script.py
        - Parent Folder
            - file1
            - file2
            - file3
            - ...
"""

import os
import shutil

# =============================================================================
# SET PARAMETERS
# =============================================================================

# If you're running this standalone
if __name__ == "__main__":

    # INSERT YOUR PARENT FOLDER THAT CONTAINS YOUR LABELLED FILES HERE
    # eg. data_folder = "Parent_Folder_Name"
    data_folder = None

# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

def create_label_folders(data_folder):
    """
    Sifts through a folder of labelled data, and copy-sorts them into subfolders.

    create_label_folders(data_folder)

    This will create new folders and fill them with copies of files!!

    Parameters
    ----------
    - data_folder : str
        The name of the parent folder you want to sift through
        (eg. "Training", "Images_Images")

    Note
    ----
    Ensure your parent folders are placed in the same folder as your script

    Structure your files and folder as such:
        Root directory:
            - your_script.py
            - Parent Folder
                - file1
                - file2
                - file3
                - ...
    """

    # Parse all files in directory
    file_names = os.listdir(data_folder)

    # Define characters to replace
    replace_string = "_0123456789\\/:*?'\"<>|"

    # Define the dictionary used for console feedback
    feedback = {}

    # For each file in the parent folder
    for i, file in enumerate(file_names):
        
        # Remove all irrelevant characters to generate the final folder name
        for char in replace_string:
            file_names[i] = file_names[i].split(".")[0].replace(char, "")

        # If the relevant subfolder doesn't exist, create it
        if not os.path.exists(os.path.join(data_folder, file_names[i])):
            try:
                os.mkdir(os.path.join(data_folder, file_names[i]))
                feedback[file_names[i]] = 0
            except:
                pass
            
        # Copy the files that should belong to the subfolder into the subfolder
        try:
            shutil.copyfile(os.path.join(data_folder, file),
                            os.path.join(data_folder, file_names[i], file))
            
            # And increment the value in the dictonary to keep track
            feedback[file_names[i]] += 1
        except:
            pass

    print("Label folders created:")
    for folder in feedback:
        print(folder, "|", feedback[folder], "files")

    return None

# =============================================================================
# If run as module, print the function output
# =============================================================================

if __name__ == "__main__":
    
    # Only run the function if there's a user-defined parent
    if data_folder != None:
        create_label_folders(data_folder)