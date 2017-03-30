import sys

print(sys.platform)
print(sys.version)

import os

print(os.getcwd())

print(os.environ)

print(os.getenv('MAVEN_HOME'))

import datetime


print(datetime.date.today())

print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))

import html
print(html.escape("This HTML fragment contains a <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))