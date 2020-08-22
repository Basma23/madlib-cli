import re

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

# with open('madlib_cli/files/story.txt') as file:
#     content = file.read()
    
# content

def read_template():
    file = open('madlib-cli/files/story.txt', 'r')
    content = file.read()
    return content

def parse(text):
    words = []
    replace = re.findall(r'\{.*?\}', text)
    for i in replace:
        words.append(i.strip("{ }"))
    return words

def merge(text, words):
    inputs = parse(text)
    return (re.sub(r' {[^}]*}', ' {}', text)).format(*words)

def file_copy(text):
    print(text)
    file = open('madlib-cli/files/user_story.txt', 'w')
    file.write(text)

if __name__ == "__main__":
    print(welcoming_message)
    content = read_template()
    inputs = parse(content)
    words = []
    for i in range(len(inputs)):
        words.append(input('enter a/an {} '.format(inputs[i])))
    copying = merge(content, words)
    file_copy(copying)