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

    for i in range(0,len(l)):
        l[i] = int(l[i]) 
    l= np.array(l)       
    matrix = np.matrix(l.reshape((640, 480)))
    file.close()
    return matrix

# print(np.shape(readImagePgm('pic1.pgm')))

def writeImagePgm(m, lx, ly, density):
    file = open("output.pgm", "w")
    file.write("P2")
    file.write(f'\n{lx}')
    file.write(f' {ly}')
    file.write(f'\n{density}\n')
    for x in range(lx):
        for y in range(ly):
            file.write(f'{m[x][y]} ')
    file.close()
    
# writeImagePgm(readImagePgm('pic1.pgm'), 640, 480, 255)

def mean_stdev(matrix):
    matrix = np.matrix(matrix)
    mean = matrix.mean()
    stdev = np.std(matrix)
    return mean, stdev

print(mean_stdev(readImagePgm('pic1.pgm')))