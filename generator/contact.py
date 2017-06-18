from model.contact import Contact
import random
import string
import json
import os
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#TODO: remove tailer space
testdata = [Contact(name="", surname="", address="")] + [
    Contact(name=random_string("Name",10), surname=random_string("Familia",10), address=random_string("Home",20),
            phone_home=random_string("555", 7), email=random_string("email", 20) + "@example.com")
    for i in range(5)
]


file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))