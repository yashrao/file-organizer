import os

MAIN_FOLDER = '/home/yash/Downloads'
DEST_FOLDER = '/home/yash/Downloads/Organized'

def organize():
    files = os.listdir(MAIN_FOLDER)
    for filename in files:
        if filename is 'Organized': # skip the organized folder 
            continue
        if os.path.isdir(MAIN_FOLDER + '/' + filename):
            continue # skip directories
        file_extension = filename.split('.')[-1]
        path = MAIN_FOLDER + file_extension
        filename_no_ext = ''.join(filename.split('.')[:-1])
        if file_extension is 'part': # checking if file is a .part file which is a download
            continue
        if filename_no_ext + 'part' in files: #checking if currently being downloaded
            continue
        if not os.path.exists(path):
            os.mkdir(path)

        print(file_extension + filename_no_ext)

        

if __name__ == '__main__':
    organize()
