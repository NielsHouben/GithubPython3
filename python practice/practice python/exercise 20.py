#write
open_file = open('pyTest.txt', 'w')
open_file.write(input())
open_file.close()

#read
open_file = open('pyTest.txt', 'r')
print(open_file.read())
open_file.close()
