import os

temp = "negative"
folder = f"dataset/{temp}"

for count,filename in enumerate(os.listdir(folder)):
    dst = f"{str(count)}_{temp}.pdf"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
    os.rename(src, dst)
    print(f"{str(count)}_{temp} renamed")