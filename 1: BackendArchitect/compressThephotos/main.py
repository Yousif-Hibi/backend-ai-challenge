import os



print("List of Files and Directories")
new_file= "/home/compressed"
def list_files_recursive(path='/'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            last_four = full_path[-4:]
            if last_four == ".jpg":
                file_size = os.path.getsize(full_path)
                if file_size >=1000000 :
                    new_path = os.path.join("/home/sandov/compressed", entry)
                    os.rename(full_path,new_path)
                    print(file_size )


directory_path = '/home/sandov/Pictures'
list_files_recursive(directory_path)