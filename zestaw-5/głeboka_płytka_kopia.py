import copy

li1 = [1, 2, [3, 5], 4]

li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)

li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)


print("li1 ID_new: ", id(li1), "Value: ", li1)

print("li2 ID_new: ", id(li2), "Value: ", li2)

print("li3 ID_new: ", id(li3), "Value: ", li3)

li2 = li1

li2[2][0] = 7

print("li1 ID_new_n: ", id(li1), "Value: ", li1)

print("li2 ID_new_n: ", id(li2), "Value: ", li2)

print("li3 ID_new_n: ", id(li3), "Value: ", li3)
# wyniki po kopii głębokiej:

# #li1 ID_new:  140700252230912 Value:  [1, 2, [3, 5], 4]
# li2 ID_new:  140700252230848 Value:  [1, 2, [3, 5], 4]
# li3 ID_new:  140700252951680 Value:  [1, 2, [7, 5], 4]

# wyniki po kopii płytkiej:

# #li1 ID_new:  140700252230912 Value:  [1, 2, [7, 5], 4]
# li2 ID_new:  140700252230848 Value:  [1, 2, [7, 5], 4]
# li3 ID_new:  140700252951680 Value:  [1, 2, [3, 5], 4]