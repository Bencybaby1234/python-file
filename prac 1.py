# creating file for reading and wrting
file1 = open("myfile.txt", "w")
file1.write("hello")
file1.writelines("this is delhi \n this is paris \n this is new york")
file1.close()

# read modes
file2 = open("myfile.txt", "r")
print(file2.read())

file2.seek(0)
print(file2.read(9))

file2.seek(0)
print(file2.readline(9))
