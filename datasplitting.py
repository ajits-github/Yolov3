import os
import random
import pandas as pd
import numpy as np
from shutil import copyfile

data_dir='/home/ajit/Desktop/master_project/YOLO_format_data/Images/'
# print(os.listdir(data_dir))
classes = os.listdir(data_dir)
classes.sort()
# list_to_remove = ['00000', '00001', '00002', '00003','00004','00005']
# final_list = list(set(classes) - set(list_to_remove))
# final_list.sort()
# print(final_list)
source_path = [f'/home/ajit/Desktop/master_project/YOLO_format_data/Images/{a}' for a in classes]
source_path_textfiles = [f'/home/ajit/Desktop/master_project/YOLO_format_data/Textfiles/{a}' for a in classes]
# print(source_path)
# print(source_path_textfiles)

TRAINING_PATH_DEST='/home/ajit/Desktop/master_project/coco128/images/train2017'
TEST_PATH_DEST= '/home/ajit/Desktop/master_project/coco128/images/test2017'

TRAINING_TEXT_PATH_DEST ='/home/ajit/Desktop/master_project/coco128/labels/train2017'
TEST_TEXT_PATH_DEST = '/home/ajit/Desktop/master_project/coco128/labels/test2017'


def split_data(SOURCE, SOURCE_TEXTFILE, TRAINING, TRAINING_TEXT_PATH, TESTING, TESTING_TEXT_PATH, SPLIT_SIZE):
    
    files = []
    print('Split Data')
    for filename in os.listdir(SOURCE):
        file = SOURCE +'/'+ filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")
    i,k=0,0
    training_length = int( len(files)* SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    
    print('SOURCE: ',SOURCE, '\n TRAINING', TRAINING, '\n TESTING',TESTING, '\n ',len(files))
    print('training_length:',training_length)
    print('testing_length:',testing_length)
    
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[training_length:(training_length+testing_length)]

    # print((training_set))
    # print(len(validation_set))
    # print((testing_set))
    
    for filename in training_set:
        this_file = SOURCE +'/'+ filename
        text_file_name = filename.split('.')[0]+'.txt'
        # print("text_file_name: "+text_file_name)
        text_file_source = SOURCE_TEXTFILE +'/'+ text_file_name
        # destination = TRAINING +'/'+ filename
        destination = TRAINING +'/'+ filename
        print("0000000000000000", TRAINING_TEXT_PATH)
        destination_textfile = TRAINING_TEXT_PATH +'/'+ text_file_name
        # print("this_file", this_file)
        # print("destination", destination)
        # print("text_file_source", text_file_source)
        # print("destination_textfile", destination_textfile)
        copyfile(this_file, destination)
        copyfile(text_file_source, destination_textfile)
        i+=1
        # exit()
    print(f"Number of files in Training: {len(os.listdir(TRAINING+'/'))}")
    print(f"Number of files in Training text: {len(os.listdir(TRAINING_TEXT_PATH+'/'))}")
    print(f"total for training- {TRAINING}: {i}")
         
    for filename in testing_set:
        this_file = SOURCE +'/'+ filename
        text_file_name = filename.split('.')[0]+'.txt'
        # print("text_file_name: "+text_file_name)
        text_file_source = SOURCE_TEXTFILE +'/'+ text_file_name
        # text_file = SOURCE_TEXTFILE +'/'+ text_file_name
        destination = TESTING+'/' + filename
        destination_textfile = TESTING_TEXT_PATH +'/'+ text_file_name
        copyfile(this_file, destination)
        copyfile(text_file_source, destination_textfile)
        k+=1
    print(f"Number of files in Testing: {len(os.listdir(TESTING+'/'))}")
    print(f"Number of files in Testing text: {len(os.listdir(TESTING_TEXT_PATH+'/'))}")
    print(f"total for testing- {TESTING}: {k}")

    # for filename in (os.listdir(TESTING +'/')):
    #       filename = TESTING_TEXT_PATH +'/'+filename.split('.')[0]+".txt"
    #       if (os.path.exists(filename) ) == False:
    #         print("File dosnt exist: "+filename)


split_size = .80
# source_path = "/home/ajit/Desktop/master_project/YOLO_format_data/Images/00001"
# source_path_textfiles = "/home/ajit/Desktop/master_project/YOLO_format_data/Textfiles/00001"
print('TRAINING_TEXT_PATH_DEST',TRAINING_TEXT_PATH_DEST)
for source_path,source_path_textfiles in zip(source_path, source_path_textfiles):
  
# for source_path,source_path_textfiles,TRAINING_PATH_DEST, TRAINING_TEXT_PATH_DEST, TEST_PATH_DEST, TEST_TEXT_PATH_DEST in zip(source_path,
#                                                             source_path_textfiles, TRAINING_PATH_DEST, TRAINING_TEXT_PATH_DEST, TEST_PATH_DEST, TEST_TEXT_PATH_DEST):
                                 # TRAINING_PATH,VALIDATION_PATH, TEST_PATH):
    #print('source: ',source,'\n', train_dir_path,'\n',val_dir_path,'\n')
    # print('TRAINING_TEXT_PATH_DEST',TRAINING_TEXT_PATH_DEST)
    split_data(source_path,source_path_textfiles, TRAINING_PATH_DEST, TRAINING_TEXT_PATH_DEST, TEST_PATH_DEST, TEST_TEXT_PATH_DEST, split_size)
    # split_data(source,train_dir_path,val_dir_path,test_dir_path, split_size)
    print('Splitting \n')