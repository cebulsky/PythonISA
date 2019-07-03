# old_number = 4
# new_number = old_number
# old_number = 6
#
# print(old_number)
# print(new_number)
#
# old_list = [1, 2, 3]
# new_list = old_list
#
# old_list[0] = 4
#
# print(old_list)
# print(new_list)
#

import copy

nested_list = [ [ [2, 3, 45], 2, 3] ]
new_list = copy.deepcopy(nested_list)

new_list[0][0][1] = 36

print(nested_list)
print(new_list)