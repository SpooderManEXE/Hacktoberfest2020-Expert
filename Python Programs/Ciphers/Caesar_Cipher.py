In this cipher, alphabet in the plain text is shifted by a fixed number down the alphabet(can be called as Key).

alphabets='abcdefghijklmnopqrstuvwxyz'

#Ask the user for the input string and stores it in variable string_input.
string_input=str(input("Enter your text that you want to convert:")) 

#Key denotes the number of shifts user wants.
key=int(input("Enter the key value:"))

#initialise an empty variable output to store the output
output=""
n=len(string_input)                              #calculates the length of string so that loop works according to the length of string.

for i in range(n):
    character=string_input[i]
    location=alphabets.find(character)           #to find the location as per alphabets. 
    new_loc=(location+key)%26                    #after shifting acording to key it stores the new location.
    print("character",character,"location",location,"new location",new_loc)
    output+=alphabets[new_loc]                    #assigns all the result to output

print(output)                                     #prints the final output
