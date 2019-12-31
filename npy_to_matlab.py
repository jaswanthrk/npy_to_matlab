#!/usr/bin/env python

import sys
import scipy.io
import numpy as np
import os

def npy_to_matlab(NAME, type):
    if type == 'folder' : 
        FOLDER = NAME
        files = (os.listdir(FOLDER))
        path = os.path.join(os.getcwd(),FOLDER)
        npyFiles=[]
        matStructure = {}
            
        for f in files:
            # print(f)
            extension = os.path.splitext(f)[1]
            if extension == '.npy':
                npyFiles.append(f)
        
        if not npyFiles:
            print("Error: There are no .npy files in %s folder"%(FOLDER))
            sys.exit(0)
        print('The input files are : {}'.format(npyFiles))
        
    else : 
        FILE = NAME
        path = os.getcwd()
        matStructure = {}
        npyFiles = [FILE]
        print('The input files are : {}'.format(npyFiles))
    

    print('The output files are : ')
    for f in npyFiles:

        name = os.path.splitext(f)[0]
        currentFile= os.path.join(path,f)   
        variable = os.path.splitext(f)[0]
        
        #MATLAB only loads variables that start with normal characters
        variable = variable.lstrip('0123456789.-_ ')
        
        try:          
            values = np.load(currentFile)
        except IOError:
            print("Error: can\'t find file or read data")
        
        else:
            matStructure[variable] = values

    filename = name + '.mat'
    print(filename + '\n')
    if matStructure:
        scipy.io.savemat(filename, matStructure)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python %s output_filename "%(sys.argv[0]))
        sys.exit(0)
    
    NAMES = sys.argv[1:]
    print('\nThe arguments are : {} \n'.format(NAMES))

    for NAME in NAMES:
        if not os.path.exists(NAME):
            print('No such folder or file exists..')

        if os.path.isdir(NAME):
            print('The FOLDER : {}'.format(NAME))
            npy_to_matlab(NAME, 'folder')

        if os.path.isfile(NAME):
            print('The FILE : {}'.format(NAME))
            npy_to_matlab(NAME, 'file')
