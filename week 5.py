# WEEK 5
# 1. working with text files
# 1.1 computer files:
#  --> used to store information as binary data, a sequence of 0 and 1
#  --> Applications ( e.g. Microsoft Word) convert these bytes (binary data) into something humans can understand.
# 1.2 open() function --> built-in function
#  --> file: the items saved in computer's storage
#  --> file object : a python object which allows us access file on the computer
#  --> file object opens a line of communication between the file and Python
#  --> the communication flow is from the file to Python
#  --> open()function can return the information stored in the file
#      as either raw bytes( bytes object) or decoded text (str object)
# Example :
fobj = open('qan_stk_prc.csv', mode = 'rt')
# --> r :reading mode: we can only open and read, can't write to the file
# --> t : text mode: automatically convert from bytes to text(str object)
# --> open() return/assign the file object to the variable fobj
# --> access mode >> r: open for reading / default value for the access mode
#                 >> w : open for writing/ erase any previous content if any
#                 >> a : open for writing/ appends content to the end of the file
# --> data type >> t : text data / default value for the data type
#               >> b : binary data
# in-class exercise 1 :
fobj = open('qan_stk_prc.csv', mode= 'rt')
fobj = open('qan_stk_prc.csv', mode= 'wb')
fobj = open('qan_stk_prc.csv', mode= 'at')

# read( )method
cnts= fobj.read()
# to check if the file is stll opened in python
print(fobj.closed)
# to close a file
fobj.close()
print(fobj.closed)
# --> for loop to read the content of a file one at a time
# fobj = open('file', mode='r')
# for line in fobj:
#     print(line)
# ⚠️cnts = fobj.read()

# 1.3 context manager
#  --> it is important to close a file
#  --> it is easy to forget to close a file, so need a context manager
#  --> how to use it ? with open() as fobj:

# in-class exercise 2
def freqword(filepath):
    with open(filepath) as file:
        counts= dic()
        for line in file:
            words = line.split()
            for word in words:
                counts[word]= counts.get(word,0)+1

        maxcount = None
        maxword = None
        for word, count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
    return (f'the most frequent word is {maxword}, and the number of times appeared is {maxcount}')
freqword('/Users/zhouyaqi/PycharmProjects/toolkit/data/new_file.txt')

# 2. Pandas
# definition : Pandas is a Python package providing fast, powerful and flexible open source data analysis and
#              manipulation tool.