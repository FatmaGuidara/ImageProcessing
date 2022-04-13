import numpy as np

def readImagePgm(file_name):
    file = open(file_name, "r")
    # reading each line  
    lines = file.readlines() 
    # removing comments
    for line in list(lines):
        if(line[0]=='#'):
            lines.remove(line)
    # list of numbers
    l = []
    for line in list(lines):
        # reading each word        
        for word in line.split():
            # displaying the words           
            l.append(word)      
    p = l[0]
    if (p!='P2' and p!='P5'):
        print('Insupported format')
        exit()
    del(l[0])
    
    lx = int(l[0])
    del(l[0])

    ly = int(l[0])
    del(l[0])

    density = int(l[0])
    del(l[0])

    matrix = []

    for x in range(lx):
        row = []
        for y in range(ly):        
            row.append(int(l[0]))
            del(l[0])
        matrix.append(row)
    return matrix

print(np.shape(readImagePgm('pic1.pgm')))

