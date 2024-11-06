"""
This function reconstructs a sentence by joining words in the 'words' list
according to the lengths in 'lengths' provided
"""
def RebuildSentence ( words,lengths ):
    new_list = []
    for i in range ( len(words) ):
        word = words [i]
        length = lengths [i]
#if is needed to validate the length if it exceeds the word length
        if length > len (word):
            length = len (word)
        count = ""
        for j in range ( length ):
            count += word[j]
            new_list.append(count)
#to rebuild the sentence
    final_result = " "
    for i in range ( len(new_list) ):
        final_result = final_result + " " + new_list[i]
    return final_result

list_of_words = ["The","sky","is","blue"]
list_of_length = [3,2,4,1]
#if is needed to validate the input
if len ( list_of_words) != len ( list_of_length ):
    print (" Words and lengths list must have the same length!")
else:
    result = RebuildSentence ( list_of_words,list_of_length )
    print ( result )
