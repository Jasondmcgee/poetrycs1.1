import random

poem_list = []


def startup():
    userinput = input("would you like to write your own poem? type yes to write your own.")
    
    if (userinput == 'yes'):
        poem = input('write your poem! dont be afraid to get creative:)')

    else:
        filee = open("poem.txt", "r")
        poem = filee.read()

    for line in poem.splitlines():
            poem_list.append(line)

def lines_printed_backwards(poem_list):
    artwork = " "
    artwork = artwork.join(poem_list[::-1])
    print(artwork)

def lines_printed_random(poem_list):
    masterpiece = []
    artwork = " "
    for line in poem_list:
        index = random.randint(0, len(poem_list)-1)
        masterpiece.append(poem_list[index])
        
    artwork = artwork.join(masterpiece)
    print(artwork)

def words_printed_random(poem_list):
    divided = []
    randomized = []
    output = ' '
    for line in poem_list:
        divided.append(line.split(' '))
    
    for line in divided:
        for word in line:
            word = line[random.randint(0, len(line)-1)]
            randomized.append(word)
    output = output.join(randomized)
    print(output)

startup()
words_printed_random(poem_list)
