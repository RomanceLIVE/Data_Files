import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)

#testing app
if __name__ == "__main__":
    archive_path = r"C:\Users\Robert\PycharmProjects\pythonProject\Projects\File_compressor\compressed.zip"
    dest_dir = r"C:\Users\Robert\PycharmProjects\pythonProject\Projects\File_compressor"

    extract_archive(archive_path, dest_dir)

# we used "\\" instead of "\" because of Unicode escape sequence
# now the change with "\\" created a new issue where i cant select zips from the file explorer
# reason why i go back to absolute path and use "r" in front of the path
# which will treat the syntax literraly and not interpret any special letters/symbols
# to avoid the Unicode issue