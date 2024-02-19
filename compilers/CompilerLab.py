import sys

#assigning the file inputs from terminal into variables 
input_file = sys.argv[1]
output_file = sys.argv[2]

#checking that there are the correct amount of inputs 
if len(sys.argv) != 3:
    print("Please enter in the corrext format")
    sys.exit(1)

#open the files 
in_file = open(input_file, "r")
out_file = open(output_file, "w")

#read the lines in the file 
linesa = in_file.readlines()
holder = 0
#loop through each line in the file 
for line in linesa:
    if line != '\n':
        #if the current line node number is not bigger than the previous line node
        if int(line.split()[0]) <= int(holder):
            print('Please put the numbers in ascending order')
            #stop the program as it is not in ascending order
            sys.exit()
        else:
            holder = int(line.split()[0])
print('Lines were in ascending order')

#reset the readlines pointer to the top of the file 
in_file.seek(0)
linesb = in_file.readlines()
count = 0
#if the number of lines exceeds 50
for line in linesb: 
        count += 1
if count <= 50:
    print("File has 50 or fewer lines.")
else:
    print("File has more than 50 lines.")
    
#reset the readlines pointer 
in_file.seek(0)
lengthArray = []
holderArray = []
actualArray = []
#loop through each line in the file 
for line in in_file:
    if line == '\n':
        continue
    #split the numbers on each line up using the spaces
    a = line.split()
    #assign these values to an array
    actualArray.append(a)
    #get the number at the start of the line
    startNumber = line.split()[0]

    #if the array is empty (the first item)
    if len(lengthArray) == 0:
        #append the node number and the how many neighbours it has 
        lengthArray.append(str(line[0]) + ' ' + str(len(a)))
        holderArray.append(startNumber)

    else:
        #loop through the array
        for i in range(len(lengthArray)):
            #put the nodes in the array in descending order 
            if len(a) > int(lengthArray[i].split()[1]):

                if(startNumber not in holderArray):
                    #insert at the index i 
                    lengthArray.insert(i, str(startNumber) + '  ' + str(len(a)))
                    holderArray.append(startNumber)

            elif i == len(lengthArray) - 1:
                lengthArray.insert(i + 1, str(startNumber) + ' ' + str(len(a)))
                holderArray.append(startNumber)

checked = [] #this is where we add all of the starting indexes that have been assigned a character

#loop through the array 
for i in range(len(lengthArray)):
    usedColours = []
    notFound = True
    toAscii = chr(ord("A"))

    #assign A to the starting node (now in descending order)
    if i == 0:
        lengthArray[i] = str(lengthArray[i]) + " A"
        #append A to the colours that have been checked
        checked.append(lengthArray[i].split()[0])
    
    #if the node is not the first node
    else:
        #find the position of the node in the 2D array
        for q in range(len(actualArray)):
            if actualArray[q][0] == lengthArray[i].split()[0]:
                #loop through the nodes neighbours
                for k in range(len(actualArray[q])):
                    #creating list of used colours 
                    #if the neighbour has already been assigned a colour 
                    if str(actualArray[q][k]) in checked:
                        for elem in lengthArray:
                            #find out what colour it was assigned 
                            if str(elem.split()[0]) == str(actualArray[q][k]):
                                #append this colour of the neighbour to the used colours array
                                usedColours.append(elem.split()[2])
           
        if i != 0:
            #while the colour that hasnt been used by the neighbours isnt found
            while notFound:
                usedColours = sorted(usedColours)
                #if the usedColours array isnt empty
                if usedColours:
                    #loop through the used colours
                    for l in usedColours:
                        #if our ascii value is in the used colours array 
                        if toAscii == l:
                            #plus one to the ascii value so it looks at the next letter
                            toAscii = chr(ord(toAscii) + 1)
                            #if the ascii value is above 90 that means we would have to use more than 26 colours which isnt possible
                            if ord(toAscii) > 90:
                                print('Algorithm cannot produce a result with 26 colours or less')
                                #stop the loop and exit the program
                                notFound = False
                                sys.exit()
                        else:
                            notFound = False
                else:
                    lengthArray[i] = str(lengthArray[i]) + " A"
                    checked.append(lengthArray[i].split()[0])
                    notFound = False

            #assign the ascii value which wasnt used by the neighbours to the correct node
            lengthArray[i] = str(lengthArray[i]) + ' ' + str(toAscii)
            #append this new ascii value to the checked array
            checked.append(lengthArray[i].split()[0])

#sort the array based on the nodes in ascending order
mainArray = sorted(lengthArray, key=lambda x: int(x.split()[0]))

#loop through this sorted array and write them to the output file 
for p in range(len(mainArray)):     
    out_file.write(str(mainArray[p].split()[0]) + str(mainArray[p].split()[2]) + '\n')
    








