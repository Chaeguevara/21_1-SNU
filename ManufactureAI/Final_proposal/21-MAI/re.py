# importing os module
import os
  
# Function to rename multiple files
def main():
    desiredPath="./original"
    newFiles = sorted(os.listdir(desiredPath))
    for count, filename in enumerate(newFiles):
        # dst ="Hostel" + str(count) + ".jpg"
        # src ='xyz'+ filename
        # dst ='xyz'+ dst
        print(filename)
        # rename() function will
        # rename all the files
        os.rename(desiredPath + "/" + filename, desiredPath + "/" + str(count)+ ".jpg")
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()