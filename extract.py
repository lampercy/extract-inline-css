import pdb
import sys
import re
import string
import random

def gen_cname():
    return ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in range(8))

def main(path):
    f = open(path, 'rb')
    regex = re.compile(r'style\s*\=\s*\"[^\"]+\"')
    text = f.read()

    styles = {}
    result = re.search(regex, text)
    while result:
        cname = gen_cname()
        chtml = "class=\"%s\"" % cname
        text = re.sub(regex, chtml, text, 1)
        styles[cname] = result.group(0)
        result = re.search(regex, text)

    pdb.set_trace()

if __name__ == "__main__":
    main(sys.argv[1])
