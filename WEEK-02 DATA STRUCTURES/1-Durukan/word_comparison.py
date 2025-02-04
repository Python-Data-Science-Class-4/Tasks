def word_comparison(word1, word2):
    #take the letters that make the word
    w1_letter = set([i for i in word1.lower()])
    w2_letter = set([i for i in word2.lower()])

    common_letters = "".join(sorted(list(w1_letter & w2_letter))) #intersection of letters
    unique1_letters = "".join(sorted(list(w1_letter - w2_letter))) # word1 difference word2
    unique2_letters = "".join(sorted(list(w2_letter - w1_letter)))  # word2 difference word1

    print([common_letters, unique1_letters, unique2_letters])


word_comparison(word1=input("Enter first word: "), word2=input("Enter second word: "))

''' Kod cok guzel ama bir kac onerim var.
**Set oluştururken zaten karakterlerin birbirinden farklı olduğu kabul edildiği için bir listeye çevirme işlemine gerek yok.
**common_letters, unique1_letters, ve unique2_letters listelerini oluştururken sorted fonksiyonunu direkt kullanabilirisniz
**Sonuçları bir liste olarak döndürmek ve listeyi doğrudan yazdırmak yerine, bir değişkene atayabilirsiniz.'''
