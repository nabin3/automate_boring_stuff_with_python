#! python3
# stripByRegex.py takes one string and a charset which will be replaced by empty string, and if ommitted the 2nd argument then all whitespace charachter will be trancated if exists any  

import re, sys

# strip() method implemented with regex
def stripRegex(content: str, charset: str=' ') -> str:
    """Strips leading and trailing character from a string with regex.
    Params:
        content: This is 1st parameter, it takes the string to be stripped.
        charset: This is 2nd parameter, it takes the string which will be trancated from the beginning and end of the given string. This parameter has default value of ' ', which means if only one argument provided then all leading and trailing whitespace chars from the string will be trancated.
    Returns:
        A stripped version of the string which was passed to the 1st parameter.
    """
    charsetRegex = re.compile(f'^[{re.escape(charset)}]+|[{re.escape(charset)}]+$', re.MULTILINE)
    return charsetRegex.sub('', content)

if __name__ == '__main__':
    argsLength = len(sys.argv)

    if argsLength >= 2 and argsLength <= 3:
        if argsLength == 2:
            print(stripRegex(sys.argv[1]))
        else:
            print(stripRegex(sys.argv[1], sys.argv[2]))
    else:
        print('invalid usage \n usage:// python stripByRegex.py string_to_strip charset which need to be replaced with empty string')
