def is_anagram(word1,word2):
    d1={}
    d2={}
    for i in word1:
        d1[i]=word1.count(i)
    for j in word2:
        d2[j]=word2.count(j)
    if (d1==d2):
        print("Yes")
    else:
        print('No')
        
word1=input('Enter First word: ')
word2=input('Enter second word: ')
is_anagram(word1,word2)
