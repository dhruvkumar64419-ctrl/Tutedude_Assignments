# Task 1
try:
    Dict1 = {'Dhruv': 87, 'Sonali': 95, 'Akash': 88, 'Shivam': 64}
    a = input('Enter the student\'s name: ').capitalize()
    print("{}'s marks: {}".format(a, Dict1[a]))
except KeyError:
    print('Student not found.');

# Task 2

list1 = [1,2,3,4,5,6,7,8,9]
print("Original list:", list1)
a = list1[0:5]
print("Extracted first 5 elements: ", a)
a.reverse()
print("Reversed extracted list: ", a)