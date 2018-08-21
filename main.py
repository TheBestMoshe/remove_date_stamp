#!/usr/bin/env python3.6

from os import listdir, chdir, rename, remove, walk
import os
from tkinter import filedialog
from tkinter import *

# ----------------------
#
#    CONFIGURATION
#
# ----------------------
VERBOSE = True


def clean_file_name(file_name):

    begin = file_name.find('(')
    end = file_name.find(')')

    return file_name[:begin - 1] + file_name[end + 1:]


def clean_files(files):
    completed_files = []
    changes = 0
    deleted = 0
    skiped = 0
    for file in files:
        if '(' in file and ')' in file:
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
                print(f'There is no date stamp in this file: {file}')
    return {'changed': changes,
            'deleted': deleted,
            'skiped': skiped}


def main(files):
    files.sort(reverse=True)
    counter = clean_files(files)
    return counter


if __name__ == '__main__':
    print('Welcome to the Windows File History date stamp and duplicate '
          'remover')
    input('Press "ENTER" to use the dialogue to chose the starting directory')
    root = Tk()
    root.withdraw()

    chose_file = False
    while chose_file is False:
        DIR_NAME = filedialog.askdirectory() + '/'
        print('The selected directory is: ' + DIR_NAME)
        confirm = input('Are you sure you would like to continue? y/n '
                        '("quit" to cancel) ')
        print('Confirm = ' + str(confirm))
        if confirm == 'n':
            print('Make another selection.')
        elif confirm == 'y':
            chose_file = True
        elif confirm == 'quit':
            print('Quiting...')
            quit()
        else:
            print('Input not valid. Please chose a file.')

    print('IMPORTANT: Once this program runs, the file names')
    print('and deleted files may not be recovered. This program is as is and')
    print('without any warrenties.')
    print('Changes will be made to files in ' + DIR_NAME)
    confirm = input('Are you sure you would like to proceed? y/n ')
    if confirm != 'y':
        print('Quiting...')
        quit()

    # chdir(DIR_NAME)

    file_list = []
    files = []
    test = 0
    for dirname, dirnames, filenames in os.walk(DIR_NAME):

        # get path to all subdirectories first.
        # for subdirname in dirnames:
        #     files.append(os.path.join(dirname, subdirname))

        # get path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

    counter = main(files)

    print('Files changed: ' + str(counter['changed']))
    print('Files deleted: ' + str(counter['deleted']))
    print('Files skiped: ' + str(counter['skiped']))

    print('\nQuiting')

    quit()
