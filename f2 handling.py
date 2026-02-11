print("welcome to the seek() and tell() functions")
#SEEK
with open("d.txt",'r')as f: # Move the pointer forward and backward
    f.seek(10)
    data=f.read(5)
    print(data)

#TELL
with open('b.txt','r')as f: # tell function return the current pointer position
    f.read(3)
    print(f.tell())

# TRUNCATE
with open('b.txt','r+')as f:# truncate(size) reduces the file size to the specified number of bytes.
    f.truncate(25)
    print(f.read())

    

        