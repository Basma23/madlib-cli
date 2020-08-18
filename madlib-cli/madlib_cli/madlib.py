welcoming_message = '''
***************************************************************
                   Welcome to Madlib CLI game               
    Mad Libs is a game where you fill in a bunch of blanks 
    of different word types, and then a story is generated 
    based on those words, and sometimes the story is 
    surprisingly funny.   
    Let's start
***************************************************************
'''

import re

# with open('madlib_cli/files/story.txt') as file:
#     content = file.read()
    
# content

def read_template():
    file = open('madlib_cli/files/story.txt', 'r')
    content = file.read()
    return content

def parse(content):
    words = []
    replace = re.findall(r'\{.*?\}', content)
    for i in replace:
        words.append(i.strip("{ }"))
        return words

def merge(content):
    inputs = parse(content)
    word = []
    for i in range(len(inputs)):
        word.append("enter a/an {} ".format(lst[i]))
    return (re.sub(r' {[^}]*}',' {} ',content)).format(*word)

def file_copy(text):
    print(text)
    file = open('madlib_cli/files/user_story.txt', w)
    file.write(text)

if __name__ == "__main__":
    print(welcoming_message)
    content = read_template()
    inputs = parse(content)
    copying = merge(content)
    file_copy(copying)