from clearConsole import clearConsole
clearConsole()

f = open('input.txt', 'r')
passFile = open("PassFile.txt", 'w')
filedFile =  open("FiledFile.txt", 'w')

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
        passFile.write(line)
    else:
        filedFile.write(line)

f.close()
passFile.close()
filedFile.close()
