# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:59:54 2018

@author: XiangQian
"""
import os
from tqdm import tqdm

# main_dir = Directory of main folder
main_dir = "IET_Shopee_original"
dir_to_keep = "BabyBibs"
#dir_to_keep = name of the category to keep which includes
#BabyBibs , BabyHat , BabyPants, BabyShirt , PackageFart , womenshirtsleeve , womencasualshoes , womenshiffontop , womendollshoes , womenknittedtop
#womenlazyshoes , womenlongsleevetop , womenpeashoes , womenplussizedtop , womenpointedflatshoes , womensleevesstop , womenstripedtop , wrapsnslings


def transfer_learning_folder_create():
    other_dir = "{}\{}".format(main_dir,"others")
    if "others" in os.listdir(main_dir):
        print("{} exists".format(other_dir))
    else:
        print("creating other folder")
        os.mkdir(other_dir)
    
    for subfolders in tqdm(os.listdir(main_dir)):
        if subfolders == dir_to_keep or subfolders == "others":
            pass
        else:
            for img in tqdm(os.listdir("{}\{}".format(main_dir,subfolders))):
                original_dir = "{}\{}\{}".format(main_dir,subfolders,img)
                replacement_dir = "{}\{}".format(other_dir,img)
                #print(original_dir, replacement_dir)
                os.rename(original_dir, replacement_dir)
                
            path_to_remove = "{}\{}".format(main_dir,subfolders)
            path_not_to_remove_main = "{}\{}".format(main_dir,dir_to_keep)
            path_not_to_remove_other = "{}".format(other_dir)
            if path_to_remove == path_not_to_remove_main or path_to_remove == path_not_to_remove_other:
                print("{} kept".format(path_to_remove))
                pass
            else: 
                print("{} down".format(path_to_remove))
                os.rmdir(path_to_remove)
        
def alexnet_folder_create():
    other_dir = "{}\{}".format(main_dir,"allimage")
    if "allimage" in os.listdir(main_dir):
        print("{} exists".format(other_dir))
    else:
        print("creating other folder")
        os.mkdir(other_dir)
    
    for subfolders in tqdm(os.listdir(main_dir)):
        for img in tqdm(os.listdir("{}\{}".format(main_dir,subfolders))):
            original_dir = "{}\{}\{}".format(main_dir,subfolders,img)
            replacement_dir = "{}\{}".format(other_dir,img)
            #print(original_dir, replacement_dir)
            os.rename(original_dir, replacement_dir)
            
        path_to_remove = "{}\{}".format(main_dir,subfolders)
        path_not_to_remove_other = "{}".format(other_dir)
        if path_to_remove == path_not_to_remove_other:
            print("{} kept".format(path_to_remove))
            pass
        else: 
            print("{} down".format(path_to_remove))
            os.rmdir(path_to_remove)
            
#transfer_learning_folder_create()
alexnet_folder_create()