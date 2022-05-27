# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    with open(filename) as file:
        file_to_be_read = file.read()
        return file_to_be_read

    
print(read_file_content("story.txt"))


    
    


def count_words():
    text = read_file_content("./story.txt").split(" ")

    #initialize an empty dictionary
    dictionary = dict()

    #iterate through every word in text
    for word in text:
        if word in dictionary: #check if the word is already in the dictionary
            dictionary[word] += 1 #if so, add 1 to the frequency of the word(key)
        else:
            dictionary[word] = 1 # if not, set the value of the word(key) to 1

    print(dictionary)



count_words()

