import sys
import os
import quopri
import locale
import re

lang = locale.getlocale()
messages = ('Выберите и перетащите только 1 файл.', 'There must be only 1 file to pass.')

if ( len(sys.argv) > 2 ):
	if( re.findall(r'Russian', lang[0]) ):
		print(messages[0])
		input()
	else:
		print(messages[1])
		input()

else:
	file = sys.argv[1]
	filename, extension = os.path.splitext(file)
	filename_copy = filename + "_copy" + extension
	fout = open(filename_copy, "w")

	with open(file, "rt") as f:
		data = f.read()
		change_version = data.replace("VERSION:2.1", "VERSION:3.0")
		remove_symbols = change_version.replace("=\r\n", "")
		utf = quopri.decodestring(remove_symbols)
		text = utf.decode("utf-8")
		fout.write(text)
		f.close()
