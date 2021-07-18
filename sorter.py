import glob, os, shutil

def makeDir(dirName):
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, "in ", folder, " Created ")    

my_dir = os.getcwd()

all_folders = os.listdir()

dir_videos = 'Videos'
dir_photos = 'Photos'

photos_filetypes = ["*.tiff", "*.tif", "*.bmp", "*.jpg", "*.jpeg", "*.gif", "*.png", "*.dng", "*.CR2"]
videos_filetypes = ["*.mp4", "*.mov", "*.wmv", "*.avi", "*.mkv", "*.3gp", "*.webm", "*.mpeg", "*.HEIC"]

for folder in all_folders:
    print("Currently in folder ", folder, "\n")
    try:
        folder_path = my_dir + "\\" + folder
        os.chdir(folder)
        # print(os.getcwd())
        # Make the folders if they don't already exist
        try:
            makeDir(dir_videos)
        except FileExistsError:
            print("Directory " , dir_videos , "in ", folder, " already exists")

        try:
            makeDir(dir_photos)
        except FileExistsError:
            print("Directory " , dir_photos , "in ", folder, " already exists")
            

        print("Now moving files!")

        destinationVideos = folder_path + "\\" + dir_videos
        destinationPhotos = folder_path + "\\" + dir_photos

        print("Destination for photos: ", destinationPhotos)
        print("Destination for videos: ", destinationVideos)

        print("\nMoving videos!")

        for name in videos_filetypes:
            for file in glob.glob(name):
                shutil.move(file, destinationVideos)   

        print("\nMoving photos!")

        for name in photos_filetypes:
            for file in glob.glob(name):
                shutil.move(file, destinationPhotos)

    except NotADirectoryError:
        print("This file is not a directory!")
    os.chdir(my_dir)
    print("\n")
    print("****************************************************************")
    print("\n")