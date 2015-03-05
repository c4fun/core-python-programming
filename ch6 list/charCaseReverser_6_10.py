s= 'Mr. Ed'

newStr = ''
for c in s:
	if c.isupper():
		newStr += c.lower()
	elif c.islower():
		newStr += c.upper()
	else:
		newStr += c

print(newStr)
