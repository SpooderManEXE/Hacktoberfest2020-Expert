def check_palindrome(string):
    length = len(string)
    for i in range(0,length//2):
        if(string[i] != string[length-i-1]):
            return False
    return True
string = input()
len_string = len(string)-1
executed = False
for curr_idx in range(1,len_string-1):
    if check_palindrome(string[:curr_idx]):
        for curr_idx_j in range(curr_idx+1,len(string)):
            if(check_palindrome(string[curr_idx:curr_idx_j]) and check_palindrome(string[curr_idx_j:])):
                executed = True
                print(string[:curr_idx])
                print(string[curr_idx:curr_idx_j])
                print(string[curr_idx_j:])
                break
        if(executed):
            break
if(executed==False):
    print("not possible")

