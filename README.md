# Anti-Duplicator

Script scans the folder and looks for duplicate files in that folder and all subdirectories.

# Quickstart

The script requires the installed Python interpreter version 3.6.

You have to run the script with the `-d`, `--directory` argument with path to directory.

To call the help, run the script with the `-h` or `--help` option.

```bash
$ python3 duplicates.py -h
usage: duplicates.py [-h] -d DIRECTORY

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        full path to the directory
```

# Example 

```bash
$ python3 duplicates.py -d /home/parallels/test/
Duplicates found: 
-----------------------
File with name war.txt is repeated in the following folders:
/home/parallels/test/
/home/parallels/test/test2

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
