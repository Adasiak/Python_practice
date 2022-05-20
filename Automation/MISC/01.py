from clearConsole import clearConsole
clearConsole()

f = open('inputFile.txt', 'r')
print("erroro check")

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
    
    


f.close()