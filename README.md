# Name-recognition-in-Zoom-transcripts
## About
The following script will create a new text file by replacing all the occurences of people names with a '#' symbol. <br>
The tool used for this purpose is spacy. <br>
Inaddition a text file 'All_names.txt' is created that contains all the names that have occured in the respective text files. <br>

Instructions to run the file on a Mac device

Python version used: Python 3.9.1 <br>
However, it should be compatible with other versions

## Step 1 : Install dependencies
- Install python
  Follow the steps as shown by clicking the link

  https://www.python.org/downloads/

- Install spacy:
  Go to the below link for complete instructions
  https://spacy.io/usage

  Or you could execute the following lines in your terminal
  ```
  $ pip install -U pip setuptools wheel
  $ pip install -U spacy
  $ python -m spacy download en_core_web_sm

  ```
## Step 2 : Save files in the appropriate folder

- Here the 'Data' folder consists of all the text files
- Save the 'Data' folder and python script (recognize_name.py) in the same folder
  e.g. the file path could be as follows
  
  ```
  ‘/Users/xyz/Code for name recognition/’

  ```
  Here, the 'Data' folder and 'recognize_name.py' is saved in the the folder 
  'Code for name recognition' <br>
  e.g. the file structure is as follows
  
  ```
  - Code for name recognition
    - Data
      - file1.txt
      - file2.txt  
    - recognize_name.py
  ```
## Step 3 : Execute the python script

Ways to execute the file
1. To run through the python shell i.e. press Fn + 5 key or click on Run Module in the Python IDLE

OR

2. To run through the terminal cd to the directory where the folder exists
i.e. on the terminal
To find the file path on Mac 
  Refer the following <br>
  https://support.apple.com/guide/mac-help/get-file-folder-and-disk-information-on-mac-mchlp1774/mac

  - On your Mac, in a Finder window or on the desktop, select the item.
  - Choose File > Get Info, or press Command-I.
  - An information window opens for the item. 
  - Copy the contents in Where section in the Data info window that's the file path.

Now on the terminal, <br>
Replace the file path with the path you obtained in the previous step

```
% cd 'file path'  
% python recognize_name.py

```
The output should be as follows

```
Enter the folder name Data
Directory 'Modified_files' created successfully
All the files have been modified and have been saved to the 'Data/Modified_files' directory
```
-----------------------------------------------------------------------------------------------
New files should have been created in the 'Data/Modified_files' directory <br>
All_names.txt <br>
file1_modified.txt <br>
file2_modified.txt

