import os
import sys
import shutil
import argparse
import send2trash

def usage():
  print("[+] python file.py <folderName> permanently-delete -> to permanently delete the repeated files")
  print("[+] python file.py <folderName> delete -> to send the repeated files to trash/recycle bin")
  sys.exit()

if len(sys.argv) != 3:
  usage()

files_list = []

try:
  for dirname, folders, files in os.walk(sys.argv[1]):
    for f in files:
      if f in files_list:
        try:
          print("folder path: {}".format(os.path.join(dirname, f)))
          if sys.argv[2].lower() == 'delete':
            send2trash.send2trash(os.path.join(dirname, f))
          elif sys.argv[2].lower() == 'permanently-delete':
            os.remove(os.path.join(dirname, f))
          else:
            usage()
          print("[=] {arg}d file path: {fn}".format(arg=sys.argv[2], fn=os.path.join(dirname, f)))
        except Exception as error:
          print(error)
          print("[-] Exiting the program...")
          sys.exit()
      else:
        files_list.append(f)

  for dirname, folders, files in os.walk(sys.argv[1]):
    for folder in folders:
      try:
        if sys.argv[2].lower() == 'delete':
          send2trash.send2trash(os.path.join(dirname, folder))
        elif sys.argv[2].lower() == 'permanently-delete':
          os.rmdir(os.path.join(dirname, folder))
        else:
          usage()
      except Exception as error:
        pass
  
  print("[+] Successfully completed the task!!!!!...")

except FileNotFoundError as error:
  print(error+"\n")
  print("[-] Folder path mentioned doesn't exists")
  sys.exit()