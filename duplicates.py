import os
import sys
import argparse
from collections import defaultdict


def find_duplicates(directory_path):
    files_info = defaultdict(list)
    for path, dirs, filemanes in os.walk(directory_path):
        for filename in filemanes:
            files_info[(filename,
                        os.stat(os.path.join(path, filename)).st_size)].append(path)
    return {file_info: paths for file_info, paths
            in files_info.items() if len(paths) > 1}


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
    if not os.path.isdir(directory_path):
        sys.exit("Directory {} doesn't exist! Try another directory!"
                 .format(directory_path))
    else:
        duplicates = find_duplicates(directory_path)
    if duplicates:
        print('Duplicates found: ')
        print('-----------------------')
        for file_info, paths in duplicates.items():
            filename, _ = file_info
            print('File with name {} is repeated in the following folders:'
                  .format(filename))
            print('\n'.join(paths))
        print('_______________________')
    else:
        print('No duplicates found')
