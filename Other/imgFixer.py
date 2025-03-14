import os
from PIL import Image 


OUTPUT = "./output/"


def remove_dark(img, name):
    img = Image.open(img)
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 

    newData = [] 

    for item in datas:
        if item[0] <= 56 and item[1] <= 56 and item[2] <= 56:
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)

    rgba.putdata(newData) 
    rgba.save(f"{OUTPUT}{name}", "PNG") 
    return


def remove_white(img, name):
    img = Image.open(img)
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 

    newData = [] 

    for item in datas: 
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)

    rgba.putdata(newData) 
    rgba.save(f"{OUTPUT}{name}", "PNG") 
    return


def remove_grey(img, name):
    img = Image.open(img)
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 

    newData = [] 

    for item in datas: 
        if item[0] == 128 and item[1] == 128 and item[2] == 128:
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)

    rgba.putdata(newData) 
    rgba.save(f"{OUTPUT}{name}", "PNG") 
    return


def remove_blue(img, name):
    img = Image.open(img)
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 

    newData = [] 

    for item in datas: 
        if (120 <= item[0] <= 165) and (200 <= item[1] <= 260) and (200 <= item[2] <= 255):
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)

    rgba.putdata(newData) 
    rgba.save(f"{OUTPUT}{name}", "PNG") 
    return


def fix_types():
    files = os.listdir("./img/types/")

    for f in files:
        remove_dark("./img/types/" + f, f)
    return


if __name__ == "__main__":
    remove_blue("./img/foo.png", "foo.png")