# -*- coding: utf-8 -*-
"""
generate_label_dicts()
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
This importable module defines a function that generates enumerated
dictionaries of label folders from a list of parent folders.

It can be run either standalone or as a module!

Functions:
- generate_label_dicts(label_folder_list[, headers = None])

Note:
Ensure your parent folders are placed in the same folder as your script

Structure your files and folder as such:
    Root directory:
        - your_script.py
        - Parent Folder
            - <0_label_name>
            - <1_label_name>
            - <2_label_name>
            - ...
"""

import os
import glob
from pprint import pprint
import shutil

# =============================================================================
# SET PARAMETERS
# =============================================================================

# If you're running this standalone
if __name__ == "__main__":
    # INSERT YOUR WANTED FOLDERS HERE
    label_folders = ["Training"]

data_folder = None

# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

def get_label_dicts(label_folder_list, headers = None):
    """
    Get enumerated dictionaries of label folders from a list of parent folders.

    generate_label_dicts(label_folder_list[, headers = None])

    The IDs generated are numbered from 0, and alphabetically sorted.

    Parameters
    ----------
    - label_folder_list : list of str
        The list of parent folder names (eg. "Training", "Labels")

    - headers : str, optional
        The dictionary type you wants
        - None - Returns both dictionary versions
        - Labels - Returns a dictionary with labels as keys, IDs as values
        - IDs - Returns a dictionary with IDs as keys, labels as values

    Returns
    -------
    - label_dict : dict
        Dictionary with labels as keys, IDs as values
        (IDs are ints that start from 0)

    - id_dict : dict
        Dictionary with IDs as keys, labels as values
        (IDs are ints that start from 0)

    Note
    ----
    Ensure your parent folders are placed in the same folder as your script

    Structure your files and folder as such:
        Root directory:
            - your_script.py
            - Parent Folder
                - <0_label_name>
                - <1_label_name>
                - <2_label_name>
                - ...
    """

    # Get a list of the relevant folder paths
    paths = [os.path.join(os.path.abspath(""), folder) for folder in label_folder_list]

    # Initialise output dictionaries
    label_dict = {}
    id_dict = {}

    # Filter out non-folders
    label_folders = [folder for folder in glob.glob(paths[0] + "\*") if os.path.isdir(folder) == True]

    # For each folder, generate the relevant dictionaries
    for i, folder in enumerate(label_folders):

        # Just take the names of the folders as the keys
        id_dict[i] = folder.split("\\")[-1]
        label_dict[folder.split("\\")[-1]] = i

    if headers == "Labels":
        return label_dict

    elif headers == "IDs":
        return id_dict

    else:
        return label_dict , id_dict

# =============================================================================
# If run as module, print the function output
# =============================================================================

if __name__ == "__main__":
    # Print the label dictionaries!
    print("LABELS:")
    pprint(get_label_dicts(label_folders, "Labels"))

    print("\nIDs:")
    pprint(get_label_dicts(label_folders, "IDs"))