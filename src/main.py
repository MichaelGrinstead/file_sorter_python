from utils import *
import shutil


def main():
    dir = input("Enter a directory: ")
    files = list_files(dir)

    extensions = get_file_extensions(files)
    print(extensions)

    for extension in extensions:
        create_directory(os.path.join(dir, extension))

    for file in files:
        file_folder = os.path.splitext(file)[1][1:]
        src = os.path.join(dir, file)
        dst_dir = os.path.join(dir, file_folder)
        dst = os.path.join(dst_dir, file)
        print(f"Moving {file} to {file_folder}")
        shutil.move(src, dst)


main()
