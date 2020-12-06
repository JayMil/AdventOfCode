import re

p = re.compile("1\d[2-9]\d|200[0-2]")
m = p.match("3920")

if (not m):
    print("True")
else:
    print("False")
