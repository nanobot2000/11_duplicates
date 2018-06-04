import os
import argparse


def find_duplicates(files_info):
    seen = dict()
    for path, file in files_info:
        if file in seen.keys() and seen[file]['size'] == os.stat(os.path.join(path, file)).st_size:
            print(os.path.join(path, file), ' and ', os.path.join(seen[file]['path'], file), ' are duplicates!')
        else:
            seen[file] = {'path': path, 'size': os.stat(os.path.join(path, file)).st_size}
    return None


def scan_folder(folder):
    return [(path, file) for path, dirs, files in os.walk(folder) for file in files]


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', help='full path folder', required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argparser()
    files = scan_folder(args.folder)
    find_duplicates(files)
