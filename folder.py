import os

for i in range(1,100000):
    print(f"{i} Folder Created")
    os.mkdir(f"./{i}")
