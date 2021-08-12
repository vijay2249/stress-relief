import os
import sys
import hashlib
import send2trash

def usage():
  print("[+] python file.py <folder1> <folder2> <folder3> delete -> to permanently delete the repeated files")
  print("[+] python file.py <folder1> <folder2> <folder3> trash -> to send the repeated files to trash/recycle bin")
  print("[+] python file.py <folder1> <folder2> <folder3> print -> to just print the repeated files")
  print("[+] You can enter as many folders as you can")
  sys.exit()

def printResults(files):
  print('[+] The following files are identical. The name could differ, but the content is identical')
  print('-------------------')
  for f in files:
    for i in f:
      print('\t{}'.format(i))
    print('-------------------')

def trashFiles(files):
  for f in files:
    for i in f[1:]:
      print("[=] Trashing {} file".format(i))
      send2trash.send2trash(i)
    print("_________________")
    print("[+] {} duplicates of this file are send to trash".format(f[0]))
  print("[+] Successfully deleted all the duplicate files....YAY!!!!!!!!")

def deletePermanently(files):
  warnAgain = str(input("[-] Are you sure to delete files permanently(yes/no): "))
  while warnAgain.lower() not in ['yes', 'no', 'y', 'n']:
    warnAgain = str(input("[-] Are you sure to delete files permanently(yes/no): "))
  if warnAgain.lower() in ['yes', 'y']:
    print("[-] Deleting duplicate files permanently......")
    for f in files:
      for i in f[1:]:
        print("[=] Deleting {} file".format(i))
        os.remove(i)
        print("_________________")
      print("[+] {} duplicates of this file are permanently removed successfully".format(f[0]))
  else:
    print("[=] Please check once again before you are sure to delete files [=]")

def hashfile(path, blocksize = 65536):
  afile = open(path, 'rb')
  hasher = hashlib.md5()
  buf = afile.read(blocksize)
  while len(buf) > 0:
    hasher.update(buf)
    buf = afile.read(blocksize)
  afile.close()
  return hasher.hexdigest()

def findDuplicates(parentFolder):
    # Dups in format {hash:[names]}
  copies = {}
  for dirName, subdirs, fileList in os.walk(parentFolder):
    print("Scanning {}".format(dirName))
    for filename in fileList:
      path = os.path.join(dirName, filename) # Get the path to the file
      file_hash = hashfile(path) # Calculate hash
      # Add or append the file path
      if file_hash in copies:
        copies[file_hash].append(path)
      else:
        copies[file_hash] = [path]
  return copies

def delete_Empty_Folders(Folders):
  for i in Folders:
    for dirname, folders, files in os.walk(i):
      for folder in folders:
        try:
          path = os.path.join(dirname, folder)
          os.rmdir(path)
          print("[+] Deleted empty folder {}".format(path))
        except Exception as error:
          continue

# storing files in parent dictionary
def joinDicts(parentDict, childDict):
  for key in childDict.keys():
    parentDict[key] = childDict[key] if key not in parentDict else parentDict[key]+childDict[key]

if __name__ == '__main__':
  if len(sys.argv) > 2 and sys.argv[-1].lower() in ['trash', 'delete', 'print']:
    duplicate_files = {}
    folders = sys.argv[1:-1]
    for i in folders:
      if os.path.exists(i):
        joinDicts(duplicate_files, findDuplicates(i))
      else:
        print("[-] Folder path {} does not exists".format(i))
        sys.exit()
    duplicate_files = list(filter(lambda x : len(x) > 1, duplicate_files.values()))
    if len(duplicate_files) < 0:
      print("[+] No Duplicate files found....YAY!!!!!!!!!")
      sys.exit()
    else:
      print("[+] Duplicates found...")
      if sys.argv[-1].lower() == 'print':
        printResults(duplicate_files)
      elif sys.argv[-1].lower() == 'trash':
        trashFiles(duplicate_files)
        delete_Empty_Folders(sys.argv[1:-1])
      elif sys.argv[-1].lower() == 'delete':
        deletePermanently(duplicate_files)
        delete_Empty_Folders(sys.argv[1:-1])
      sys.exit()
  else:
    usage()
