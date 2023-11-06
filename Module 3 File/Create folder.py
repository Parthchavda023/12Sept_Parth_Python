import os

##--------new folder Create krva--------#
# os.mkdir('New Folder')


# #------Sub Folder Create krva-----#
# os.chdir('New Folder')
# os.mkdir('Sub Folder')
# os.chdir('New Folder/Sub Folder')
# os.mkdir('Test Folder')


#------Folder Ni Andar File Create krva-------#
os.chdir('New Folder/Sub Folder/test Folder')
open("Newfile.txt",'x')