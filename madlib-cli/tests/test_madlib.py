from madlib_cli.madlib import read_template, parse, merge

def test_read_files():
    expected = open('madlib_cli/files/story.txt','r').read()
    received = read_template()
    assert expected == received

def test_parse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received