import os
import argparse
from collections import defaultdict


def find_duplicates(files_info):
    duplicates = defaultdict(list)
    for path, filename, size in files_info:
        duplicates[filename+', '+str(size)].append(path)
    return {key: value for key, value in duplicates.items() if len(value) > 1}


def scan_folder(directory_path):
    return [(path, filename, os.stat(os.path.join(path, filename)).st_size)
            for path, dirs, files in os.walk(directory_path) for filename in files]


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--directory',
        help='full path to the directory',
        required=True
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    argparser = create_argparser()
    directory_path = argparser.directory
    files_info = scan_folder(directory_path)
    duplicates = find_duplicates(files_info)
    if duplicates:
        print('Duplicates found: ')
        print('-----------------------')
        for file, pathways in duplicates.items():
            filename, size = file.split(', ')
            print('File with name {} is repeated in the following folders:'.format(filename))
            for path in pathways:
                print(path)
        print('_______________________')
    else:
        print('No duplicates found')
