
input_file_docs = []
with open('input_file_docs.txt') as input_file:
    for line in input_file:
        input_file_docs.append(line)

#print(input_file_docs)

string_input_file_docs = ""
for counter in input_file_docs:
    string_input_file_docs += counter

#print("\n" + string_input_file_docs )
digits = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for counter in len(string_input_file_docs):
    
    if (string_input_file_docs[ counter ] == "i"    #first checking keywords
    and string_input_file_docs[ counter+1 ] == "f" 
    and string_input_file_docs[ counter+2 ] == " "):
        print("\"if\" is a keyword.\n")
        counter += len("if")
        continue

    if (string_input_file_docs[ counter ] == "p" 
    and string_input_file_docs[ counter+1 ] == "r" 
    and string_input_file_docs[ counter+2 ] == "i"
    and string_input_file_docs[ counter+3 ] == "n"
    and string_input_file_docs[ counter+4 ] == "t"
    and string_input_file_docs[ counter+5 ] == "("):    #can allow a white space
        print("\"if\" is a keyword.\n")
        counter += len("print")
        continue

    if string_input_file_docs[counter] in digits:   #checking numbers
        
        flage_of_starting_identifier_with_number = False
        length_of_number = 0 #just initialed
        for counter2 in range( counter+1 , len(string_input_file_docs - counter)+1 ):
            
            if string_input_file_docs[counter2] in letters:
                flage_of_starting_identifier_with_number = True
                continue

            if string_input_file_docs[counter2] == " ":
                length_of_number = (counter2 - counter + 1)   #may has bug
                break 
                
        if flage_of_starting_identifier_with_number == True:
            print("There is a sintax error: starting identifier with number (" + string_input_file_docs[counter, length_of_number+1] + ") \n")
        else:
            print(string_input_file_docs[counter, length_of_number+1] + " is a number \n")

        counter += length_of_number + 1
    
    if string_input_file_docs[counter] in letters:      #checking indentifiers

        length_of_identifier = 0 #just initialed
        for counter2 in range( counter+1, len(string_input_file_docs - counter)+1 ):
            if string_input_file_docs[counter2] == " ":
                length_of_identifier = (counter2 - counter + 1) + 1     #may has bug
                break
        
        print(string_input_file_docs[counter, length_of_identifier] + " is indentifier")

    if string_input_file_docs[counter] == "(":
        print("it's an opening parantethes \n")

    if string_input_file_docs[counter] == ")":
        print("it's a closing parantethes \n")

    if string_input_file_docs[counter] == "+":
        print("it's an addition \n")
    
    if string_input_file_docs[counter] == "-":
        print("it's a subtraction \n")

    if string_input_file_docs[counter] == "=":
        if string_input_file_docs[counter+1] ==  "=":
            print("it's an equality opration \n")
        else:
            print("it's an assigning \n")

    else:
        continue