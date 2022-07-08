#!/usr/bin/env python3

import cgi
our_form = cgi.FieldStorage()
in_name = our_form.getfirst("in_name", "не задано")
in_message = our_form.getfirst("in_message", "не задано")

print("Content-type: text/html")
print()
print(in_name)