list_numbers = range(10)

list_of_squares = [];

# list_of_squares.append(2)
# list_of_squares.append(13)

# 1 solution
for number in list_numbers:
    list_of_squares.append(number ** 2)


# 2 solution
list_of_squares_2 = list(list_numbers[:])
for index, number in enumerate(list_numbers):
    list_of_squares_2[index] = number ** 2

print(list(list_numbers))
print(list_of_squares)
print(list_of_squares_2)

# 3 solution
last_list_of_squares = [x**2 for x in list_numbers]

words = ["iTs", "mE", "PytHon"]
new_words = [word.upper() for word in words]

print(new_words)
print(words)

print(last_list_of_squares)

list_1 = range(10,20)
list_2 = range(0,10)

list_sum = []

for left_element, right_element in zip(list_1, list_2):
    list_sum.append(left_element + right_element)

print(list(list_1))
print(list(list_2))
print(list_sum)