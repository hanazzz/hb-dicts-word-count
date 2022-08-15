"""Count words in file."""



# put your code here.
from re import I


def word_count(file_name):
    #open file and assign to variable
    file_counts = open(file_name)
    #create empty dict
    counts_of_words = {}
    #iterate through each line of the text file
    for line in file_counts:
        #split the line at the space
        word_list = line.split(" ")
        #iterate through each word in line_list and index into dictionary with word as key using get
        for word in word_list:
            word = word.lower().strip(".,?!\n")
            counts_of_words[word] = counts_of_words.get(word, 0) + 1
            #whatever is returned +1
    file_counts.close()

    # print dict
    # iterate through the dictionary (counts_of_words)
        # for each key, value pair in dictionary
            # print this: key value
    for word, count in counts_of_words.items():
        print(f"{word} {count}")

    # print(counts_of_words)

word_count("twain.txt")