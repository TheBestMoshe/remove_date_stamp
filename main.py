import functions as f
from os import listdir, chdir, rename, remove, walk
import os

# ----------------------
#
#    CONFIGURATION
#
# ----------------------
# DIR_NAME = '/home/moshe/Documents/.temp/file_names/'
DIR_NAME = '/media/moshe/Moshe\'s Hardrive Unlocked/My Files/Old computer backup/disk files/Shuki 2/'
VERBOSE = True


def clean_file_name(file_name):

    begin = file_name.find('(')
    end = file_name.find(')')

    return file_name[:begin - 1] + file_name[end + 1:]


def isHebrew(text):
    return any("\u0590" <= c <= "\u05EA" for c in text)


def clean_files(files):
    completed_files = []
    changes = 0
    deleted = 0
    skiped = 0
    for file in files:
        if '(' in file and ')' in file:
            if isHebrew(file) is False:
                clean_name = clean_file_name(file)

                if clean_name in completed_files:
                    remove(file)
                    deleted += 1
                    if VERBOSE is True:
                        print(f'Removed file: {file}')
                else:
                    rename(file, clean_name)
                    changes += 1
                    if VERBOSE is True:
                        print(f'Renamed {file} to {clean_name}')

                    completed_files.append(clean_name)

            else:
                skiped += 1
                if VERBOSE is True:
                    print(f'This file has Hebrew charecters. Skipping...')
        else:
            skiped += 1
            if VERBOSE is True:
                print(f'There is no date stamp in this file: {file}')
    return {'changed': changes,
            'deleted': deleted,
            'skiped': skiped}


def main(files):
    files.sort(reverse=True)
    counter = clean_files(files)
    return counter


if __name__ == '__main__':
    chdir(DIR_NAME)

    file_list = []
    files = []
    test = 0
    for dirname, dirnames, filenames in os.walk('.'):

        # get path to all subdirectories first.
        for subdirname in dirnames:
            files.append(os.path.join(dirname, subdirname))

        # get path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

    counter = main(files)

    print('Files changed: ' + str(counter['changed']))
    print('Files deleted: ' + str(counter['deleted']))
    print('Files skiped: ' + str(counter['skiped']))

    print('\nQuiting')

    quit()
