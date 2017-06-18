from model.group import Group
import random
import string
import json
import os
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/group.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # + string.punctuation
    # " " in the end of name lead to error too!
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
    for i in range(n)
]


file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)


with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))