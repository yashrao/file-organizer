import os
import shutil
import sys

MAIN_FOLDER = '/home/yash/Downloads'
DEST_FOLDER = '/home/yash/Downloads/Organized'
CATEGORIES = { \
    'Documents': ['docx', 'doc', 'odt'],
    'Disk Images': ['img', 'iso'],
}

def organize():
    files = os.listdir(MAIN_FOLDER)
    if not os.path.exists(DEST_FOLDER):
        print('Creating Destination folder')
        os.mkdir(DEST_FOLDER)
    for filename in files:
        if filename is 'Organized': # skip the organized folder 
            continue
        if os.path.isdir(MAIN_FOLDER + '/' + filename):
            continue # skip directories
        file_extension = filename.split('.')[-1]
        #path = MAIN_FOLDER + '/' + file_extension
        dest_path = DEST_FOLDER + '/' + file_extension
        filename_no_ext = ''.join(filename.split('.')[:-1])
        if file_extension is 'part': # checking if file is a .part file which is a download
            continue
        if filename_no_ext + 'part' in files: #checking if currently being downloaded
            continue
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
            print('creating dir ' + dest_path)
        print(file_extension + filename_no_ext)
        #shutil.move(MAIN_FOLDER + '/' + filename, \
        #        DEST_FOLDER + '/' + file_extension + '/' + filename)
        os.rename(MAIN_FOLDER + '/' + filename, \
                DEST_FOLDER + '/' + file_extension + '/' + filename)
        print('moving' + filename + ' from ' + MAIN_FOLDER + ' to ' + DEST_FOLDER + '/' + file_extension)

        

if __name__ == '__main__':
    organize()
