from madlib_cli.madlib import read_template, parse, merge

def test_read_files():
    expected = open('madlib-cli/files/story.txt','r').read()
    received = read_template()
    assert expected == received

def test_parse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received

def testMerge():
    words = ['smart', 'boxes', 'hungry', 'eat']
    text = 'A {} {} had a {} dog so they {} them'
    received = merge(text, words)
    expected = 'A smart boxes had a hungry dog so they eat them'
    assert expected == received