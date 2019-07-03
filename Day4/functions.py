def add(left_number, right_number):
    suma = left_number + right_number
    return suma

print(add(4, 2))


def repeat_n_times(word, times_to_repeat):
    # for loop to repeat (print) n times
    for i in range(times_to_repeat):
        print(word)


def split_sentence_to_words(sentence):
    words = str(sentence).split(" ")
    for word in words:
        print(word)

split_sentence_to_words("Python Day Four")