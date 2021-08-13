# stress-relief
Got bored in the first day of new semester and had to clean system for lot of copies of previous sem assignments and projects and notes, written this script to do the task for me


python delete_copies.py \<folder1> \<folder2> \<folder3> (and so on) \<print/trash/delete>

You can enter as many folders as you can, but the script checks for just the mentioned folder and its child folders, it does not include parent folder

last arguments explanation:

  print - just print the duplicate files

  trash - deletes all the duplicate files in the folder and sends them to trash/recycle bin
  
  delete - deletes the duplicate files permanently (cant be found in trash after this is executed, there is backup too in case this is just unfortunate command execution)


### Note:
previous version code just checks for the name of the file instead of the actual content of the file which is what duplicate file means, 

Executing the script did not caused any problem to me as I just copy the whole folder to another location instead of changing names of the files

And this error bounced back today while executing this on a folder with renaming the files which contains the same content inside 

