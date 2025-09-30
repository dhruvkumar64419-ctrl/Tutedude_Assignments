# Task 1
'''
try:
    file1= open ('sample.txt', 'r')
    reading_file = file1.read()
    print('Reading file content:')
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
'''
# Task 2

user_input=input('Enter text to write to the file: ')
file2= open ('output.txt', 'w')
write_to_file = file2.write(user_input)
file2.close()

print('Data successfully written to file')

append=input('\nEnter additional text to append to the file: ')
file2= open ('output.txt', 'a')
write_to_file= file2.write(append)
file2.close()

print('Data successfully appended to file')
print('\nFinal content of output.txt: ')

file2= open ('output.txt', 'r')
write_to_file = file2.read()
print(write_to_file)
file2.close()