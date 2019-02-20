f=open("hello.txt")
try:
	for line in f:
	  print line,
finally:
	f.close()
