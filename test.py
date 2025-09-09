import mymodule
import os
print(mymodule.value)

print(os.path.sep)

path = os.getcwd()
print("Current Path: ",path)
print("Basename: ",os.path.basename(path))
print("Dir: ", os.path.dirname(path))
