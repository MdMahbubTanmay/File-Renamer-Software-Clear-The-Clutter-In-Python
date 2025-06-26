import os

FileNames = os.listdir("F:/DeveloperTools/Python Learning/Folder_Xmpl")  #Here FileNames will be a list which will contain all files name of that folder

j=0

try:

 for i in FileNames:
    os.rename(f"F:/DeveloperTools/Python Learning/Folder_Xmpl/{i}",f"F:/DeveloperTools/Python Learning/Folder_Xmpl/{j}{i[len(i)-4:]}") # here {i[len(i)-4:]} mean total lenth minus 4 mean it will only kept the extension like hello.png here it will do total char here 9 and 9-4 =5 so it will get 5 to end here 5 to end is .png and that is the file extension
    j+=1
 print("Rename All Successful")


except Exception as e:
  print(e)
