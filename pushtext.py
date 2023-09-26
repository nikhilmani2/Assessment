
file1='pythonsample.txt'
file2='outputfile.txt'
file=open(file1,'r')
contents=file.read()
secondfile=open(file2,'w')
secondfile.write(contents)
file.close()
secondfile.close()


