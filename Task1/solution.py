#!/usr/local/bin/python3
'''
    * Author: Taha Magdy
    * Date: 18th Oct, 2017

    * Task1
    =======
    - Input: comma-seperated file extensions && a directory as command line.
      argument
    - Output: prints the files taged with the matching extension.


    * How to use it?
    ================
    - This script takes two command-line arguments:
        + the first arument is comma-seperated file extensions
        + the second argument is the path (without spaces)

    - If you do not pass the second argument.
        + then the current directory is set by default

    $ python extension1,...,extensionN path/to/directory
    $ python extension1,...,extensionN


    * Assumptions
    =============
    - This script runs on UNIX/Linux (I saw that in the pdf you've send me,
       Windows has different commands)
    - Path sould not contain any spaces.
    - If you used python 2.x, then you will see () arount the printed lines.
'''
from sys import argv
from os import popen


def getFileExtention(file_name):
    '''
        * Parameter: the file name
        * Return: the extension of the given file.
        * More: If the file does not has extension
                >> the file name is returned.
    '''
    extension = file_name.split('.')
    return extension[len(extension)-1]


def getDirectoryContent(directory_name):
    '''
        * Parameter: the directory name/path {without spaces}
        * Return: a list of the content of the directory.
    '''
    list_content = "ls " + directory_name
    return popen(list_content).read().strip().split("\n")


def support_ancillary(extension, ancillary, dict):
    '''
        * this to support other extension [ancillary]
          with the current [extension] like > .h with .c and so on.
        * Parameter 1: extension that you want to add ancillary to.
        * Parameter 2: the ancillary externsion
        * Parameter 3: the dictionary {externsions: [files.extension]}
    '''
    if ancillary in dict:
        dict[extension] += dict[ancillary]
        del dict[ancillary]
        return dict
    else:
        return dict


def showResults(dict, given_extensions):
    '''
        * It just loops over the dictionay {extension: [files.extension]
          and print the results each extension with the correspoding extension.
    '''
    dict = support_ancillary('c', 'h', dict)
    dict = support_ancillary('py', 'pyc', dict)
    dict = support_ancillary('pl', 'pm', dict)
    for extension in dict:
        outputLine = ""
        extension_files = dict[extension]
        if not extension_files or extension not in given_extensions:
            continue
        else:
            outputLine += extension + ": "
            for file in extension_files:
                outputLine += file + ","
            print(outputLine.rstrip(','))


def getExtensionsInit(dict, directory_content):
    '''
        * It initialize the dict with the directory files' extensions
    '''
    for fileName in directory_content:
        extension = getFileExtention(fileName)
        dict[extension] = []
    return dict


def main():
    '''
        * Computes the task
    '''
    # Getting the command-line aruments {extension && directory}
    given_extensions = argv[1].split(",")
    directory = ''
    if len(argv) > 2:
        directory = argv[2]

    directory_content = getDirectoryContent(directory)

    # It's {extension: [file.extension}
    ext_fils_dict = {}
    ext_fils_dict = getExtensionsInit(ext_fils_dict, directory_content)

    #  putting the files in a proper place/extension in the dictionary
    #  O(n) one pass
    for file in directory_content:
        file_extention = getFileExtention(file)
        if file_extention == file:
            continue
        elif file_extention in ext_fils_dict:
            ext_fils_dict[file_extention].append(file)
        else:
            continue

    # Showing the output
    showResults(ext_fils_dict, given_extensions)


if __name__ == "__main__":
    main()
