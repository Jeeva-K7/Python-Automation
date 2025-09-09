import os
import sys
import datetime
req_path = input("Enter Path: ")
age = 3
if not os.path.exists(req_path):
  print("Not a Valid Path")
  Sys.exit(1)
if os.path.isfile(req_path):
  print("It's File, Provide Directory")
  sys.exit(2)
today = datetime.datetime.now()
for each_file in os.listdir(req_path):
  each_file_path = os.path.join(req_path, each_file)
  file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
  print(each_file_path,"\t", (today-file_cre_date).days)
