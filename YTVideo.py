'''
File I/O using Python
- with open block, closing file. 
- how to read text files
- performing basic operations (slicing, indexing, methods)
- how to write to text files (append vs write)
    - savings new files 
'''


with open ("newfile.txt", 'r') as file:
    var = file.read()
    print(type(var))
    file.close()
    pass 
