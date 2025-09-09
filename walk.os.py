import os
#path = os.getcwd()
for r,d,f in os.walk("home/rootkid/")
  for file in f:
	print(os.path.join(d,file))
