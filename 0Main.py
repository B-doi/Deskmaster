'''

██████╗░███████╗░██████╗██╗░░██╗███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░
██╔══██╗██╔════╝██╔════╝██║░██╔╝████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║░░██║█████╗░░╚█████╗░█████═╝░██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██║░░██║██╔══╝░░░╚═══██╗██╔═██╗░██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝███████╗██████╔╝██║░╚██╗██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║
╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
version 1.0

(ascii art from: https://fsymbols.com/generators/carty/)
'''
import os
import subprocess
import shutil
script_path = os.path.dirname(os.path.abspath(__file__)) #path to this file
saver_path = script_path + "\saver.bat" #this file is responsable for saving desktops

# print("changing desktops too often (more than once every 30 sec) will temporarly disable your wallpaper (atleast if you are using Lively Wallpaper)")
# print("if this occurs just put them them back on again")
print("⚠️⚠️ LOADING AND MOVING WILL BRIEFLY KILL THE WINDOWS FILE EXPORER, make sure nothing is being uploaded/downloaded/deleted/moved around as it may corrupt the data ⚠️⚠️")
"""
def listDesks_old():
    '''
    :return: Lists all of the current folders in desktop (assumed to be desktop_files)
    '''
    global script_path
    folder_path = script_path + "\Desktops"
    file_list = os.listdir(folder_path)
    return file_list
#Retired because it listed all files instead of just directories
"""
# currentDesktop = "currentDesk was not called"

if os.path.exists(script_path+"\Desktops") == False:
    print("\Desktops file not found, making a new one")
    os.mkdir(script_path+"\Desktops")


def currentDesk(command,data="if you see this you forgot to put the data in the write file"):
    '''
    :param command: r= read , w=write
    :param data: desktop name (useless for read)
    :return:
    '''
    global script_path
    global currentDesktop
    file_path = f"{script_path}\\data.txt"
    if command == "r":
        with open(file_path, 'r') as file:
            currentDesktop = file.read()
            return currentDesktop
    if command == "w":
        with open(file_path, 'w') as file:
            currentDesktop = file.write(data)
            # print("your current desktop is now: " + currentDesk("r") )

def listDesks(printOnly=False):
    '''
    :param printOnly: As the variable name suggests, this should only be used for printing out the current desktops.
    :return: a list of all the desktops (unless printOnly)
    '''
    global script_path
    global currentDesktop
    currentDesktop=currentDesk("r")
    directory = script_path + "\Desktops"
    entries = os.scandir(directory) #scans "/Desktops" directory
    directories = [entry.name for entry in entries if entry.is_dir()] #lists all folders

    if printOnly == True:
        '''
        This effectively make a fake list because lists do not like ANSI escape sequences
        '''
        new_directories = []
        for entry in directories:
            new_directories.append(entry)
            if entry == currentDesktop:
                index = directories.index(entry)
                directories[index] = '\033[4m' + entry + '\033[0m'

        print("Current desktops: [",end="")
        for entry in directories:
            if entry is not directories[-1]:
                print("\'" + entry + "\'", end=",")
            else:
                print("\'" + entry + "\'", end="")
        print("]")
    if printOnly == False:
        return directories
# print('\033[4m' + ' entry ' + '\033[0m')

def save(word2):
    global script_path
    global saver_path
    SatisfactoryExit= False
    #word2 = filename (in this case)
    while SatisfactoryExit== False:
        if word2 is not False: #if the filename is not the False
            if word2 in listDesks(): #if the file already exists (duplicate)
                desks = listDesks()
                desks_loop = 0
                word2_base = word2
                while word2 in desks: #if the itterated filename is STILL a duplicate
                    desks_loop += 1
                    word2 = word2_base + "("+ str(desks_loop) +")" #if the filename already exists make a new one like windows does save for the space between the base filename and iterated number.

                os.mkdir(path=f"{script_path}\\Desktops\\{word2}") #makes directory in which the registry will be saved
                print(f"Saved in:\"{script_path}\\Desktops\\{word2}\" as \"{word2}\" because \"{word2_base}\" was taken")

                currentDesk("w",word2) #changes current desktop to the saved desktop
                SatisfactoryExit= True
            else:
                os.mkdir(path=f"{script_path}\\Desktops\\{word2}") # creates folder
                print(f"Saved in:\"{script_path}\\Desktops\\{word2}\" as \"{word2}\"")

                currentDesk("w",word2) #changes current desktop to the saved desktop
                SatisfactoryExit= True

        else:
            word2 = input("please specify a filename: ") #in case user has not given a filename at the start

    #after a folder has been made
    subprocess.call(saver_path) #calls upon the filesaver bat file
    source = f"{script_path}\\DesktopIconLayoutSave.reg"
    destination = f"{script_path}\\Desktops\\{word2}"

    shutil.move(source, destination)

def load(word2):
    global script_path
    global saver_path
    reg_file_directory = f"{script_path}\\Desktops\\{word2}\\DesktopIconLayoutSave.reg"
    SatisfactoryExit= False
    print("")
    while SatisfactoryExit== False:
            if word2 in listDesks():
                print(reg_file_directory)
                subprocess.call(['reg', 'import', reg_file_directory]) #merges reg file

                # restarts Windows File Explorer
                # os.system("taskkill /f /im explorer.exe")
                # os.system("start explorer.exe")

                currentDesk("w",word2) #changes current desktop in the data.txt file
                SatisfactoryExit = True
            else:
                try: #checks if there are any desktops avalable, 99% better way to do it but good enough.
                    currentList = listDesks()[0]
                except:
                    currentList = False

                if currentList != False: #if a desktop does exist
                    # print(listDesks())
                    word2 = input("please specify which desktop you would like to load: ") #in case user has not given a filename at the start
                else: #if there is no desktop
                    print("There are no desktops for you to load, use \"save\" to save your current desktop")
                    SatisfactoryExit = True
def move(word3):
    """
    WARNING: STANDARDS CHANGE
    :param word2: current desktop
    :param word3: is actually word2 (the second word in the command)
    was originally meant to do something else, kept word2 and word3 as is for because lazy
    :return:
    """
    global script_path
    global saver_path
    currentList = listDesks()
    currentList_len = len(currentList)

    word2= currentDesktop

    SatisfactoryExit= False
    print("")

    if currentList_len == 0:
        print("What are you exactly trying to move? you have no desktops, go make some (use the \"save\" functiion)")
        SatisfactoryExit = True

    if currentList_len == 1:
        print("Move to what? You only have one desktop")
        save(word3)
        print("there... much better")
        SatisfactoryExit = True

    while SatisfactoryExit== False:
        if word2 not in currentList:
            print(f"your current desktop ({currentDesktop}) is not in the list (the desktop you will overwrite)")
            print(f"Desktops: " + str(listDesks()))
            word2 = input("Select a desktop to overwrite from the list above: ")

        elif word3 == False:
            print("you have not selected a desktop")
            print(f"Desktops: " + str(listDesks()))
            word3 = input("Select a desktop from the list above: ")

        elif word3 not in currentList:
            print(f"The desktop you have selected ({word3}) is not avalable")
            print(f"Desktops: " + str(listDesks()))
            word3 = input("Select a desktop from the list above: ")

        elif word2 == word3:
            print(f"The desktop you have selected ({word3}) is the same desktop as the currentDesktop ({currentDesktop}) ")
            print(f"Desktops: " + str(listDesks()))
            word3 = input("Please select another desktop: ")

        else:
            #this long ass if statement means, if both word2 and word3 exist, if both can be found in listDesks(), and they are not the same file
            old_file_directory = f"{script_path}\\Desktops\\{word2}"
            new_reg_file_directpry = f"{script_path}\\Desktops\\{word3}"
            shutil.rmtree(old_file_directory) #Deletes the word2 directory and everything inside of it
            save(word2) #makes the word2 directory again , saving the current desktop
            load(word3) #loads the word3 directory
            print(f"current desktop was saved to {word2} and now {word3} was loaded")

            SatisfactoryExit= True

def helpprint():
    print("Current commands are:")
    print("+==========================================================+")
    print("IMPORTANT: DESKTOP NAMES SHOULD NOT HAVE SPACES")
    print("save [desktop name] - Saves the current desktop")
    print("load [desktop name] - loads a desktop")
    print("move [desktop name] - Overrides [currentDesktop] and loads [desktop name]")
    print("help - prints the command list again")
    print("(list/get) - lists the desktops and your currentDesktop without the formatting stuff without ASCII escape sequences, if "+ '\033[4m' + "this" + '\033[0m' " isn't underlined, use \"list\" and \"get\" to see your desktops")
    print("+==========================================================+")
# currentDesktop = "Desk1test"
# print(f"Welcome to deskmanager, your current desktop is: \"{currentDesktop}\" ")

helpprint()

while 1:
    print("\n")
    print("████████████████████████████████████████████████████████")
    desksCount = len(listDesks())
    if desksCount != 0:
        listDesks(printOnly=True) #prints out the desktops and underlines the current one
        print("")
    else:
        print("There are no desktops, please make a desktop using the \"save\" function")
    # print("")
    currentinput = input("Command: ")
    print("████████████████████████████████████████████████████████")
    inputsplit = currentinput.split()
    inputsplit_len = len(inputsplit)
    word1 = inputsplit[0]

    iterateInput = 0
    for max in range(0, 3):
        if iterateInput < inputsplit_len:
            exec(f"word{iterateInput + 1} = '{inputsplit[iterateInput]}'")
        else:
            exec(f"word{iterateInput + 1} = {bool(False)}")
        iterateInput += 1

    #just checking how many items and assigning them to a variable, could have used
    # try:
    #     word2 = inputsplit[1]
    # except:
    #     word2 = False
    #     pass
    #
    # else:
    #     try:
    #         word3 = inputsplit[2]
    #     except:
    #         word3 = False


    if word1 == "get" or word1 == "list":
        currentDesk("r", word2)
        print(f"Desktops: " + str(listDesks()))
        print(f"your current desktop is:  \"{currentDesktop}\" ")
        if currentDesktop not in listDesks():
            print("Note: the file to your current desktop does not exist, however its name is still saved in the data.txt file.")
    elif word1 == "save":
        save(word2)
    elif word1 == "load":
        load(word2)
    elif word1 == "move":
        move(word2)
    elif word1 == "help":
        helpprint()
    else:
        print("Command is invalid or a typo was made, try again...")

