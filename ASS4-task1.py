filename="sample.txt"
try:
    file1=open('sample.txt','r')
    print("Reading file contents:")
    line_number=1
    for line in file1:
        print(f'Line{line_number}:{line.strip()}')
        line_number+=1
    file1.close()
except FileNotFoundError:
    print('the file',filename,' was not found')