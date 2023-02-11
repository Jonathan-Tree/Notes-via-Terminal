#!/usr/bin/python

import sys

for line in sys.stdin:
	if 'q' == line.rstrip():
		f.close()
		break
	else:

		print(f'New Note: {line}')
		
		note = "- " + line + "\n"
		f = open("/home/tree/.notes.md", 'a')
		f.write(note)


print("Safed")
