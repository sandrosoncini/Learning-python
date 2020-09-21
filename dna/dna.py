from collections import OrderedDict
from json import loads, dumps
from sys import argv
import sys
import csv

#check if has the correct amount of arguments
def check_input_files(argv):
    if(len(argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
    else:
        open_files()
# check with try and expect if the progrma are able to open the files
def open_files():
    try:
        database = open(argv[1], "r")
        sequence = open(argv[2], "r")
        read_files(database, sequence)
    
    except FileNotFoundError:
        print("File Not Found ")
        
#read files anf load it into memory        
def read_files(database, sequence):
    #read database into dictionary and sequence 
    db_reader = csv.DictReader(database)
    s_reader = csv.reader(sequence)
    
    #reade senquence into string
    s = None
    for row in s_reader:
        s = row[0]
    
    # loop to get teh strs into a list of names and ge the database strs    
    dna_db = {}
    strs = []
    b = True
    for i, row in enumerate(db_reader):
        if b:
            for col in row:
                if col not in strs:
                    strs.append(col)
                elif col in strs:
                    b = False
                    break
            
        dna_db[row["name"]] = row      

    sequence_count = get_counter_strs(s, strs)    
    find_match(sequence_count, loads(dumps(dna_db)))
    
# count each str into a dictionary 
def get_counter_strs(s, strs):
    strs.pop(0)
    strs_count = {}
    
    for item in strs:
        strs_count[item] =  counting(item, s) 
       
    return strs_count

#check the sequence how many specific str have in the sequence given         
def counting(strs, s):
    arr = []
    count = 0
    rep = s.replace(strs, '1')
    
    for item in rep:
        if item is '1':
            count += 1
        elif item != '1':
            arr.append(count)
            count = 0
            
    return max(arr)
    
#find the match between teh database and sequence     
def find_match(seq, db):
    
    bk = True
    for name, info in db.items():
        del info["name"]
        
        for key in info:
             info[key] = int(info[key])
             
        if info == seq:
            print (name)
            bk = False
            break
    if bk:
        print("No match.")
    


check_input_files(argv)

