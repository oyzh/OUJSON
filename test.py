import sys
from Token import *
from Parse import *

if __name__ == '__main__':
    fd = open(sys.argv[1])
    content = fd.read()
    token = Token(content)
    parse = Parse(token)
    result = parse.parse()
    print result
