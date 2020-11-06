# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#


# Read temps.txt and print it without the blank line at the end
# with open('temps.txt') as file_object:
#    contents = file_object.read()
# print(contents.rstrip())
# print('cat')

# Read temps.txt line by line and print with no whitespace
# with open('temps.txt') as file_object:
#    for line in file_object:
#        print(line.rstrip())

# Make a list of lines from the file
with open('temps.txt') as file_object:
    line_list = file_object.readlines()
print(line_list)

# Edit the elements to eliminate whitespace in the list
with open('temps.txt') as file_object:
    line_list = file_object.readlines()

list_length = len(line_list)
for i in range(list_length):
    line_list[i] = line_list[i].rstrip()
print(line_list)

# writing to empty file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I'm tired of Zoom.")
    file_object.write("hi")
# Note: files can be opened in read ('r), write ('w') or append ('a') modes. Default is read-only.
# Also note - you can only write strings this way. Data will need to be converted to str format


# Writing to an empty file
with open('sample.txt', 'w') as file_object:
    file_object.write('Is it break time yet?')



