import os
import shutil
import pyuac


def main():
    # Specify the paths to the directories, make sure they are in the format C:/Users/User/Downloads and not C:\Users\User\Downloads
    download_folder_path = "" # Download folder path here
    desktop_folder_path = "" # Desktop folder path here
    picture_folder_path = "" # Path to where you would like pictures stored

    clean_desktop_pictures(desktop_folder_path, picture_folder_path)
    clean_downloads_pictures(download_folder_path, picture_folder_path)


def clean_desktop_pictures(desktop_folder_path, picture_folder_path):
    picture_extensions = ['.png', '.jpg', '.JPG', '.PNG', '.gif', '.GIF', '.img', '.IMG','.jpeg','.JPEG']
    desktop_files = os.listdir(desktop_folder_path)
    for file in desktop_files:
        for ext in picture_extensions:
            if file.endswith(ext):
                shutil.move(desktop_folder_path + "/" + file, picture_folder_path)

def clean_downloads_pictures(download_folder_path, picture_folder_path):
    picture_extensions = ['.png', '.jpg', '.JPG', '.PNG', '.gif', '.GIF', '.img', '.IMG','.jpeg','.JPEG']
    download_files = os.listdir(download_folder_path)
    for file in download_files:
        for ext in picture_extensions:
            if file.endswith(ext):
                shutil.move(download_folder_path + "/" + file, picture_folder_path)


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
        main()
    else:
        main()
