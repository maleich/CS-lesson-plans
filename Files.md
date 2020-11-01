# Reading from & Writing to Files
This document is written to be used with the File Intro assignment, but can be applied to other situations as well. Note that the files mentioned are specific to this assignment and you will need to use different names if
 you are using different files.
## Reading a file
First, be sure the file you want to read is a .txt file and is in the same directory as your .py file. As we start
 working with files, your repos will have .txt files pre-loaded in them. As we progress, you may need to upload your
  own files. 

To open and read the `temps.txt` file, be sure you have the correct assignment open and then enter the following into
 PyCharm:
```python
with open(temps.txt) as file_object:    # opens the file and assigns it to file_object
    contents = file_object.read()       # reads the entire file and assigns it to contents
print(contents)
```
 
Note that the keyword `with` closes the file after it has been read. This helps avoid improperly closed files.


 