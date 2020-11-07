# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# PCC


# Read temps.txt and print it without the blank line at the end
# with open('text_files/temps.txt') as file_object:
#    contents = file_object.read()
# print(contents.rstrip())
# print('cat')

# Read temps.txt line by line and print with no whitespace
# with open('text_files/temps.txt') as file_object:
#    for line in file_object:
#        print(line.rstrip())

# Make a list of lines from the file
with open('text_files/temps.txt') as file_object:
    line_list = file_object.readlines()
print(line_list)

# Edit the elements to eliminate whitespace in the list
with open('text_files/temps.txt') as file_object:
    line_list = file_object.readlines()

list_length = len(line_list)
for i in range(list_length):
    line_list[i] = line_list[i].rstrip()
print(line_list)

# writing to empty file
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I'm tired of Zoom.")

# Note: files can be opened in read ('r), write ('w') or append ('a') modes. Default is read-only.
# Also note - you can only write strings this way. Data will need to be converted to str format


# Writing multiple lines
with open('text_files/sample.txt', 'w') as file_object:
    file_object.write('Is it break time yet?')
    file_object.write("hi")

# Note that all lines are stuck together. Add \n to the ends!
with open('text_files/sample.txt', 'w') as file_object:
    file_object.write('Is it break time yet?\n')
    file_object.write("hi\n")
# write as many lines as once but must be before closing file

# Appending to file
with open('text_files/sample.txt', 'a') as file_object:
    file_object.write('A cup of tea would be nice.\n')
    file_object.write('A walk would be good too.\n')


