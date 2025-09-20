import os
import shutil

# ask user for folder path
folder_path = input("Enter folder path: ")


if not os.path.exists(folder_path):
    print("Folder not found!")
else:
   
    categories = {
        "Images": [".jpg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Music": [".mp3", ".wav"]
    }

    log_file = open("log.txt", "w")

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        
        if os.path.isdir(file_path):
            continue

        moved = False
        for folder, ext_list in categories.items():
            if file.lower().endswith(tuple(ext_list)):
                new_folder = os.path.join(folder_path, folder)
                os.makedirs(new_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(new_folder, file))
                log_file.write(f"{file} → {folder}\n")
                moved = True
                break

        if not moved:  
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))
            log_file.write(f"{file} → Others\n")

    log_file.close()
    print("Files organized successfully! Check log.txt")
