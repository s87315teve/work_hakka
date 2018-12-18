import zipfile

file = open( 'baito.txt', 'r')
file2 = open('output.txt','w')
file_input=[]
line = file.readline()
while line:
    file_input.append(line)
    line = file.readline()
file.close()


for inn in file_input:
    first_file=[]
    filename=[]
    tempfilename=[]
    temp=0
    for i in range(0,len(inn)):
        for k in range (0,18):
            first_file.append(inn[k])
        if len(inn)==19:
            file2.write(''.join(first_file)+'.jpg\n')
            break
        with zipfile.ZipFile(''.join(first_file)+'.zip', 'w') as zf:
            while temp<len(inn):
                tempfilename=[]
                for k in range (0,18):
                    tempfilename.append(inn[temp+k])
                    filename=''.join(tempfilename)+'.jpg'
                #print(filename)
                zf.write(filename)
                temp=temp+19
        #print('完成 '.join(first_file)+'.zip')
        file2.write(''.join(first_file)+'.zip\n')
        break
file.close()
file2.close()
print('OK')    


