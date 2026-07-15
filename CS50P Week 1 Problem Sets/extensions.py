# prompts user for file name
file = str(input("File: "))

file = file.lower().strip()

# splits file by file name and file type
name, type , extra = file.split(".")
# image - gif, jpg, jpeg, png
# application - zip, pdf, 
# text - txt

print(type)

if extra == "":

    if type == "":
        print("application/octet-stream")
        
    if type == "gif":
        print("image/gif")
        
    if type == "jpg" or "jpeg":
        print("image/jpeg")
        
    if type == "png":
        print("image/png")
        
    if type == "zip":
        print("application/zip")
        
    if type == "pdf":
        print("application/pdf")
        
    if type == "txt":
        print(f"text/{name}")
        
else:
    
    if extra == "pdf":
        print("application/pdf")
        