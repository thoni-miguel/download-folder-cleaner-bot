# Dev: Thoni Araujo
import pathlib
import shutil

# Directories
download_folder = "C:\\Users\\wanok\\Downloads"
source_dir = pathlib.Path(download_folder)
images_folder = pathlib.Path(f"{download_folder}\\images")
videos_folder = pathlib.Path(f"{download_folder}\\videos")
audios_folder = pathlib.Path(f"{download_folder}\\audios")
documents_folder = pathlib.Path(f"{download_folder}\\documents")
applications_folder = pathlib.Path(f"{download_folder}\\applications")

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                    ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf",
                    ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".epub"]

# supported App types
application_extensions = [".exe"]

files_moved = 0
folders_created = 0


# Create the specified folder based on the existing files
def create_folders(folder):
    global folders_created
    try:
        folder.mkdir(parents=True, exist_ok=True)
        folders_created += 1
    except Exception as e:
        print(f"Exception caught: {e}")


# Get all files based on the extensions provided
def return_filenames(extensions: list[str]) -> list[pathlib]:
    found_files = []
    for extension in extensions:
        found_files.extend(source_dir.glob("*" + extension))
    return found_files


# Move the specific file to its destination folder
def move_files(files: list[pathlib], destination_folder: pathlib):
    create_folders(destination_folder)
    global files_moved
    for file in files:
        try:
            shutil.move(file, destination_folder)
            files_moved += 1
        except Exception as e:
            print(f"Something went wrong: {e}")


# check for images
def check_images():
    files = return_filenames(image_extensions)
    if files:
        move_files(files, images_folder)


# check for videos
def check_videos():
    files = return_filenames(video_extensions)
    if files:
        move_files(files, videos_folder)


# check for audios
def check_audios():
    files = return_filenames(audio_extensions)
    if files:
        move_files(files, audios_folder)


# check for documents
def check_docs():
    files = return_filenames(document_extensions)
    if files:
        move_files(files, documents_folder)


# check for applications
def check_apps():
    files = return_filenames(application_extensions)
    if files:
        move_files(files, applications_folder)


def main():
    check_images()
    check_videos()
    check_audios()
    check_docs()
    check_apps()
    print(f"Folders created: {folders_created}")
    print(f"Files moved: {files_moved}")


if __name__ == "__main__":
    main()
