# Working with files

# Reading files - review
filename = 'text_files/sample.txt'
'''
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    content_list = file_object.readlines()
print(content_list)
'''

# Writing to files
with open(filename, 'w') as file_object:
    file_object.write('Is it lunch time yet?')

with open(filename, 'w') as file_object:
    file_object.write('Is it nap time yet?\n')
    file_object.write("Yay it's Tuesday!\n")

# Appending to files
with open(filename, 'a') as file_object:
    file_object.write('What are you doing this afternoon?\n')