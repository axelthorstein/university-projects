def write_ascii_triangle(outfile, block, sidelength):
    """ (file open for writing, str, int) -> NoneType
    
    Precondition: len(block == 1)
    
    """
    
    i = sidelength
    while i > 0:
        outfile.write(i * block + '\n')
        i = i - 1
        
        
__name__ == "__main__"

outfile = open('file', 'w')
write_ascii_triangle(outfile, '@', 4)
outfile.close()
outfile = open('file', 'r')
line = outfile.read()
print(line)