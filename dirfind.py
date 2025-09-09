import os
req_path = input("Req Path: ")
req_ex = input("Req extension: ")
if os.path.isfile(req_path):
  print(f"Given {req_path} is file")
else:
  all_file_ds = os.listdir(req_path)
  if len(all_file_ds)==0:
    print("File is empty")
  else:
    req_files=[]
    for each in all_file_ds:
      if each.endswith(req_ex):
        req_files.append(each)
    for each in req_files:
      print(each, end="\t")
