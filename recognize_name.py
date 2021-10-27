'''
Python script to recognize names in a text file within a folder
To run through the python shell i.e. press Fn + 5 key or click on Run Module
>>>
Enter the folder name Data
Directory 'Modified_files' created successfully
All the files have been modified and have been saved to the 'Data/Modified_files' directory

or to run through the terminal cd to the directory where the folder exists
% python recognize_name.py
Enter the folder name Data
Directory 'Modified_files' created successfully
All the files have been modified and have been saved to the 'Data/Modified_files' directory

'''
import spacy
import os
import sys
import re
import glob

nlp = spacy.load('en_core_web_sm')

def replace_string(filename):
    f = filename.partition('/')[2]
    new_f = f[:-4]+'_modified.txt'
    # add files to the new folder: "modifiled files"
    new_filename = os.path.join(new_folder, new_f)
    if os.path.exists(new_filename):
        print("File '%s' already exists, cannot make the changes" %new_filename)
        sys.exit()
    else:
        append_write = 'w' # make new file if not

    to_match = re.compile(r'^[A-Za-z]+\s*[A-Za-z]*:')
    with open(filename, 'r') as firstfile, open(new_filename, append_write) as secondfile:
        # read content from first file
        for line in firstfile:
            new_line = re.sub(to_match, '#: ', line)
            # append content to second file
            secondfile.write(new_line)

    with open(new_filename, 'r+') as file:
        given_text = file.read()

    person_names = 'All_names.txt'
    create_person_name_file = os.path.join(new_folder, person_names)
    with open(create_person_name_file, 'a') as file_person_name:
        file_person_name.write('All names in the file ' + new_filename + "\n")
        person_name = ", ".join(find_people(given_text, new_filename))
        file_person_name.write(person_name)
        file_person_name.write("\n")
        
def find_people(text, new_filename):        
    doc = nlp(text)

    # person names
    persons = set(ent.text for ent in doc.ents if ent.label_ == 'PERSON')

    # if tag == 'PERSON' then replace it with a '#'
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            text = text.replace(ent.text, '#')
    
    with open(new_filename, 'r+') as f:
        f.seek(0)
        f.write(text)
        f.truncate()
    
    return persons


# ask for filename    
folder_path = input('Enter the folder name ')
folder_path += '' if folder_path[-1] == '/' else '/'
# read all the text files in the folder
text_files = glob.glob(folder_path+'*.txt')
# create a new folder to save the modified text files
new_folder_name = 'Modified_files'
new_folder = os.path.join(folder_path, new_folder_name)

try:
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        print("Directory '%s' created successfully" % new_folder_name)
        # call the name recognizer function on each of the files
        for fname in text_files:
            replace_string(fname)
        print("All the files have been modified and have been saved to the '%s' directory" %new_folder)
    else:
        print("Directory '%s' cannot be created as it already exists" % new_folder_name)    
except OSError as error:
    print(error)
