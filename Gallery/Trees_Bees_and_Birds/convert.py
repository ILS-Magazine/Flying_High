import os

def main():
  
    for filename in os.listdir("Images"):
        print('<img src= "Images/'+filename+'" alt="Images/'+filename+'">')
        #dst ="Hostel" + str(count) + ".jpg"
        #src ='Images'+ filename
        #dst ='Images'+ dst
          
        # rename() function will
        # rename all the files
        #os.rename('Images/'+ filename, 'Images/'+ filename.title())
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
