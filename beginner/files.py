f = open('wasteland.txt', mode='wt', encoding='utf-8')

f.write('What are the roots that clutch, ')

f.write('what branches grow\n')

f.write('Out of this stony rubbish? ')

f.close()


# to read a file
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.read())

g.close()

# g.readline() is used to read lines from a file one by one
# g.readlines() returns an array with each line as a single item

# to append to an existing file open it with mode a

h = open('wasteland.txt', mode='at', encoding='utf-8')

h.writelines(
    [
        'Son of man, \n',
        'You cannot say, or guess, ',
        'for you know only,\n',
        'A heap of broken images, ',
        'where the sun beats\n'
    ]
)
h.close()
