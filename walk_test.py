import os
path = os.getcwd
def print_tree(root):
  for dirpath, dirnames, files in os.walk(root):
    level = dirpath.replace(root, "").count(os.sep)
    indent = " "*4*level
    print(f"{indent}{os.path.basename(dirpath)}/")
    subindent = " "*4*(level+1)
    for f in files:
      print(subindent+f)
print_tree("/home/rootkid/Downloads")
