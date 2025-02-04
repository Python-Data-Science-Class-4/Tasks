# Common features of words
 
word1 = input('Enter the 1st word:')     # The user is asked for two words that he wants to compare with the input.
word2 = input('Enter the 2nd word:')
''''''
A = set(word1.lower())     
B = set(word2.lower())

difference_1 = list(A.difference(B))      # Only the letters in the first word are taken with 'difference'...
C = sorted(difference_1)
difference_2 = list(B.difference(A))      # Only the letters in the second word are taken with 'difference'...
D = sorted(difference_2)
symmetric = list(A.symmetric_difference(B))   # The symmetric difference of two words is taken... 
E = sorted(symmetric)
# These features are printed in alphabetical order in a list.
print([(''.join(C)),(''.join(D)),(''.join(E))])

''' kod gayet uzel calisiyor.
**Set islemleirni kullanarak da yapabilirsimiz. '&','-' gibi

  w1_letter & w2_letter))) #intersection of letters
  w1_letter - w2_letter))) # word1 difference word2
  w2_letter - w1_letter)))  # word2 difference word1
    
**sorted fonksiyonunu doğrudan set üzerine uygulayabilirsiniz.
**difference ve symmetric_difference sonuçlarını doğrudan bir listeye dönüştürerek bir adımı kısaltabilirsiniz.'''
