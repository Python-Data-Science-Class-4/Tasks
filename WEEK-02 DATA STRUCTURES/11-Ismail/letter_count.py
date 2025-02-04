# Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. 
# Ignore case, ignore blanks and assume the user does not enter any punctuation. Display a two-column table of the letters and their counts
# with the letters in sorted order.Example Input This is a sample text with several words This is more sample text with some different words
# Output [('a', 4), ('d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o' ,4), ('p', 2), ('r', 5),
# ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

sentencefromuser = input("Enter a sentence: ")


letter_count = {}#create a dict 

for letter in sentencefromuser:
    
    if letter.isalpha(): #Checking each letter with the isalpha() function and only processes alphabetic characters.
        
        if letter in letter_count: #Checking the letter if it is inside of sentencefromuser
            letter_count[letter] += 1 #if it is not a new letter, equals one more time 
    
        elif letter.lower() in letter_count : #And also checking each letter that they are lowercase or not.
            letter_count[letter.lower]+=1
        
        else:
            letter_count[letter] = 1 # or it is new letter, add to list   
    

sorted_counts = sorted(letter_count.items()) 

print(sorted_counts)

'''
**Odevde bizden istenen alfabetik siraya gore hangi harften kac adet kullanildigi, 
buyuk kucuk harfleri de farkli olarak hesapliyor, mesela buyuk A ile kucuk a farkliymis gibi.
bunu (letter.lower()) kullanarak cozebilirisiniz.
**Bosluk ya da farkli karakterleri de sayiyor bunu cozmek icin isalpha() fonksiyonu kullanabilirsiniz.
**Oneri olarak da get metodunu kullanarak, bir harfin zaten sözlükte olup olmadığını kontroledebilirsiniz.
Bunu zaten yapmissiniz ama sadece oneri.
Ellerinize saglik.'''
