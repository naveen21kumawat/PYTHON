import os

files = os.listdir("PYTHON/imagesFolder")

i = 1
for file in files:
    print(file)
    if file.endswith(".png"):
      os.rename(f"PYTHON/imagesFolder/{file}", f"PYTHON/imagesFolder/{i}.jpg")
    i =i+1





        
        