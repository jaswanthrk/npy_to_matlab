# npy_to_matlab
You can use this python script to convert your '.npy' file to '.mat' file.

### Usage :  

If you want to convert a 'File1.npy', 'Folder1/File2.npy' and all the npy files in the 'Folder2', then you can just call the python script as : 

__python npy_to_matlab.py  File1.npy   Folder1/File2.npy  Folder2__

#### Output : 

> The arguments are : ['File1.npy', 'Folder1/File2.npy', 'Folder2.npy']  
>  
> The FILE : File1.npy  
> The input files are : ['File1.npy'] 
> The output files are :  
> File1.mat  
>  
> The FILE : Folder1/File2.npy  
> The input files are : ['Folder1/File2.npy']  
> The output files are :   
> Folder1/File2.mat  
>  
> The FOLDER : Folder2  
> The input files are : ['File3.npy', 'File4.npy']  
> The output files are :   
> File3.mat  
> File4.mat 


### Notes :
Thanks to @ruitome. This is built on the following repository by @ruitome : https://github.com/ruitome/npy_to_matlab
