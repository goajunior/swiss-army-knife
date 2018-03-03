import sys
import os

def get_files(start_path = '.', extension = 'pdf'):

    list_of_files = []

    for path, dirs, files in os.walk(start_path):
        for filename in files:
            if filename.find(extension) != -1:
                list_of_files.append(os.path.join(path, filename))

    return list_of_files

def move_files(source_files, target_files):
    for files in source_files:
        for other_files in target_files:
            count = other_files.split('/').count(files.split('/')[2])
            print(files)
            extension = os.path.splitext(files)[1]
            name = os.path.splitext(files)[0]
            print(name)
            print(extension)
        # code...
    print(count)
    return

def check_and_rename(file, add=0):
    original_file = file
    a = 0
    if add != 0:
        split = file.split(".")
        part_1 = split[0] + "_" + str(add)
        file = ".".join([part_1, split[1]])
    if not os.path.isfile(file):
        # save here
        a = a + 1
    else:
        add = add + 1
        check_and_rename(original_file, add)
    return

def main():
    source_path = '../data/'
    source_files = get_files(source_path, 'pdf')

    print(source_files)

    # target_path  = '../data2'
    target_files = get_files('../data2/', 'pdf')

    print(target_files)

    move_files(source_files, target_files)

if __name__ == '__main__':
    main()
