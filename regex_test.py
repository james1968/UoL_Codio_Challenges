import re

txt = "Abb222"

if re.search("^([a-zA-Z0-9]{4}|[a-zA-Z0-9]{5}|[a-zA-Z0-9]{6})$", txt):
    print("true")
else:
    print("false")


