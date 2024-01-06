import os

example_dir = "/home/mike/projects/python/file_sorter/mock_desktop"


# creates a new directory at the given path
def create_directory(path):
    try:
        os.mkdir(path)
        return path
    except FileExistsError:
        print("Directory already exists")
    except OSError:
        print("Creation of the directory %s failed" % path)


# returns a list of files for the given directory
def list_files(path):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        print("Could not find directory")
        return []
    except OSError:
        print("Could not open directory")
        return []


# returns a list containing all file extensions
def get_file_extensions(files):
    extensions = []
    for file in files:
        extension = os.path.splitext(file)[1][1:]
        if extension not in extensions:
            extensions.append(extension)

    return extensions
