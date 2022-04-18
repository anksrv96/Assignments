def get_longest_word_in_current_line(data):
    list_of_words = data.split(" ")
    for i in list_of_words:
        if len(longest_word) == 0:
            longest_word.append(i)
        else:
            if len(i) > len(longest_word[0]):
                longest_word.clear()
                longest_word.append(i)
            elif len(i) == len(longest_word[0]):
                longest_word.append(i)
            else:
                continue


f = open("C:\\Users\\ashri\\PycharmProjects\\Assignments\\MyData.txt", 'r')

longest_word = []
for data in f:
    get_longest_word_in_current_line(data)

print (longest_word)
