import os
from tinytag import TinyTag as tg
import shutil
import sys
import time

def menu(user):
    print("join: t.me/TUNeHouse")
    print("Choose your unsorted music directory form the list or enter yours")
    print("1. C:\\Users\(youruser)\Downloads\Music")
    print("2. D:\Music")
    print("3. C:\\Users\\(your user)\\Music")
    print("4. C:\\Users\\(your user)\\Desktop\\Music")
    print("5. D:\Downloads\Music")
    print("6. input your self")
    print("7 or else. exit")
    choice = int(input("choose: "))
    if choice == 1:
        directory = f"C:\\Users\\{user}\\Downloads\\Music"
    elif choice == 2:
        directory = "D:\Music"
    elif choice == 3:
        directory = f"C:\\Users\\{user}\\Music"
    elif choice == 4:
        directory = f"C:\\Users\\{user}\\Desktop\\Music"
    elif choice == 5:
        directory = "D:\Downloads\Music"
    elif choice == 6:
        directory = input("enter your directory: ")
    else:
        sys.exit()
    return(directory)

def main():
    directory = menu(os.getlogin())
    try:
        os.chdir(directory)
        for f in os.listdir():
            name = os.path.basename(f)
            f_name, format = os.path.splitext(name)
            counter = 0
            if format == ".mp3" or format == ".m4a":
                counter += 1
                try:
                    audiofile = tg.get(name)
                    album = audiofile.album
                    title = audiofile.title
                    artist = audiofile.albumartist
                    if artist == None:
                        artist = audiofile.artist
                    attributes = [album, title, artist]
                    for i in range(3):
                        if attributes[i] == None:
                            attributes[i] = "Unsorted"
                        else:
                            attributes[i].strip
                    [album, title, artist] = attributes
                    address = "{}\{}".format(artist, album)
                    for special_char in ":/<>?*|\"":
                        mod_address = ""
                        for char in address:
                            if not char == special_char:
                                mod_address += char
                            elif char == "\"":
                                mod_address += "'"
                            elif char == "/":
                                mod_address += "_" 
                        address = mod_address
                                
                    try:
                        os.makedirs(address)
                    except OSError:
                        print("directory existed")
                    src_dir = "{}\{}".format(os.getcwd(), name)
                    des_dir = "{}\{}\{}".format(os.getcwd(),address,name)
                    des_dir2 = "{}\{}\{}".format(os.getcwd(),address,"{}{}".format(title,format))
                    for special_char in "/<>?*|\"":
                        mod_des_dir2 = ""
                        for char in des_dir2:
                            if not char == special_char:
                                mod_des_dir2 += char
                            elif char == "\"":
                                mod_des_dir2 += "'"
                        des_dir2 = mod_des_dir2
                    try:
                        shutil.move(src_dir, des_dir)
                        os.rename(des_dir, des_dir2)
                    except FileNotFoundError:
                        print(f'file not found error for {name}')
                    except OSError:
                        print(f'OS error for {name}')
                except ValueError:
                    print(f'error in sorting {f_name}')
                except AttributeError:
                    print(f'error in sorting {f_name}, please check the tags')
        if counter>0:
            print("%i song(s) sorted" %counter)
        else:
            print("***warning %i music file found***" %counter)
        time.sleep(3)
    except FileNotFoundError:
        print("directory does not exist")
        time.sleep(3)
        main()
        
if __name__ == "__main__":
    main()