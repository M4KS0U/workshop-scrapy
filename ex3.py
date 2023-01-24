anagram = []
def anagrams(word_A, list_B) :
    for w_2 in list_B:
        if sorted(word_A.lower()) == sorted(w_2.lower()):
            anagram.append((w_2))

    print(anagram)