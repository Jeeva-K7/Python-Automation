import os
import subprocess
sourcePath = "/home/rootkid/"
desPath = "/home/rootkid/Python Automation"

for filename in os.listdir(sourcePath):
  if filename.endswith(".py"):
    source_file = os.path.join(sourcePath, filename)
    des_file = os.path.join(desPath, filename)
    subprocess.run(['mv', source_file, des_file])

