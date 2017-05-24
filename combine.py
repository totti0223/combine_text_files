# coding: UTF-8
import os,sys

argvs = sys.argv
argc = len(argvs)
if argc ==1:
    print("must include path. ex. python \thisfile.py\ DIR/OF/FOLDER/WITH/TXT. ending program")
    quit()

if os.path.exists(argvs[1]) is False:
    print ("not a valid directory provided. ending program")
    quit()

print ("parsing",argvs[1])
    
files = os.listdir(argvs[1])

op = open("output.txt","w") #output file
for file in files:
    name, ext = os.path.splitext(file)
    if ext == ".txt":#parse only text file
        f=open(file,encoding='utf-16')
        lines = f.readlines() #read one line per line
        f.close()
        i=0
        for line in lines:
            if i == 0:
                i+=1
                continue
            #print (line)
            line = line.split(";")
            #print (line[2])
            out = name + ", " + line[2]
            op.write(out)
            i+=1
op.close()