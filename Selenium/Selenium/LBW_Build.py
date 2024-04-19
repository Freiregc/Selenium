import pyautogui
import time
import os

def find_files_with_extension(directory, extension):
    """
    Find files with a specific extension in a directory.
    
    Args:
        directory (str): The directory to search.
        extension (str): The file extension to filter by.
        
    Returns:
        list: A list of filenames with the specified extension.
    """
    matching_files = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            filename = filename.replace('.vi','')
            matching_files.append(filename)
    return matching_files

def find_files_with_directory(directory, extension):
    # Initialize an empty list to store the full paths of matching files
    matching_files = []

    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Iterate over each file in the current directory
        for file in files:
            # Check if the file has the desired extension
            if file.endswith(extension):
                # If the file matches the extension, add its full path to the list
                file_path = os.path.join(root, file)
                matching_files.append(file_path)

    return matching_files

def vi_open(archieve):
    
    os.startfile(archieve)

directory = r'C:\Users\sn1076327\Desktop\Teste de Projeto LBW com biblioteca compactada\Pasta Dados\Receitas_teste'
extension = ".vi"  # Change this to the extension you want to search for
files_name = find_files_with_extension(directory, extension)
files_directory = find_files_with_directory(directory, extension)

for filed, filen in zip(files_directory, files_name):
    vi_open(filed)
    time.sleep(12)
    # print(pyautogui.size())
    # print(pyautogui.position())
    # POSITION TO TOOLS OPTIONS 
    pyautogui.moveTo(245, 36, duration = 0.1)  
    pyautogui.click()
    #POSITION TO BUILD APPLICATION (EXE) FROM VI
    pyautogui.moveTo(307, 227, duration = 0.2)  
    pyautogui.click()
    #SAVE AS A PROJECT
    pyautogui.moveTo(962, 605, duration = 0.2)  
    pyautogui.click()
    #SAVE CHANGES
    pyautogui.moveTo(812, 437, duration = 0.2)  
    pyautogui.click()
    #TIME TO WAIT THE BUILD WINDOW OPEN
    time.sleep(8)
    #POSITION TO CONTINUE BUILD CREATE
    pyautogui.moveTo(973, 609, duration = 0.2)
    pyautogui.click()
    # POSITION TO CHANGED THE BUILD FILE NAME
    pyautogui.moveTo(787, 383, duration = 0.2)  
    pyautogui.click(clicks=2)
    pyautogui.typewrite(filen)
    time.sleep(1)
    #POSITION TO BUILD APPLICATION
    pyautogui.moveTo(1111, 785, duration = 0.2)  
    pyautogui.click()
    #TIME TO WAIT THE BUILD FINISH
    time.sleep(90)
    #POSITION TO CLICK DONE BUILD
    pyautogui.moveTo(995, 627, duration = 0.2)  
    pyautogui.click()
    #POSITION TO CLOSE PROJECT WINDOWN
    pyautogui.moveTo(1511,16, duration = 0.2)
    pyautogui.click()
    #POSITION TO SAVE THE CHANGES
    time.sleep(0.1)
    pyautogui.moveTo(633,336, duration = 0.2)
    pyautogui.click()
    #POSITION TO CLOSE LABVIEW
    pyautogui.moveTo(1354,248, duration = 0.2)
    pyautogui.click()
    #TIME TO RELOOP
    time.sleep(0.2)