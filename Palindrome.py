def is_palindrome(s): 
    #check if the string is a plaindrome 
    return s == s[::-1] #string[start:stop:step]

def PalindromeCreator(str):
    #check if the input string is already a plaindrome
    if is_palindrome(str):
        return "palindrome"
   
    for i in range(len(str)):
      modifiedstring = str[:i] + str[i+1:]#remove the character at index i
      if is_palindrome(modifiedstring):  # check if the modified string is a plaindrome
        return str[i] #return the removed character
      


#removing 2 characters
    for i in range(len(str)):
       for j in range(i+1, len(str)): 
          newstring = str[:i] + str[i+1:j] + str[j+1:] 
          if is_palindrome(newstring):
            return newstring
    return "not possible"      
      
    

myword="abcd"
result=PalindromeCreator(myword)   
print(result)   

