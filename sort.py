<<<<<<< HEAD
import os


def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == '__main__':
    files = os.listdir()
    files.remove("sort_files.py")
    print(files)
    createFolder("Images")
    createFolder("Documents")
    createFolder("Medias")
    createFolder("Others")
    imgExts = [".png", ".jpeg", ".jpg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".pdf", ".docx"]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    medExts = [".mp3", ".mp4", ".mkv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in medExts]

    print(images, documents, medias)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in medExts) and os.path.isfile(file):
            others.append(file)

    print(others)

    move("Medias", medias)
    move("Images", images)
    move("Documents", documents)
    move("Others", others)
=======
import os


def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == '__main__':
    files = os.listdir()
    files.remove("sort_files.py")
    print(files)
    createFolder("Images")
    createFolder("Documents")
    createFolder("Medias")
    createFolder("Others")
    imgExts = [".png", ".jpeg", ".jpg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".pdf", ".docx"]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    medExts = [".mp3", ".mp4", ".mkv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in medExts]

    print(images, documents, medias)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in medExts) and os.path.isfile(file):
            others.append(file)

    print(others)

    move("Medias", medias)
    move("Images", images)
    move("Documents", documents)
    move("Others", others)
>>>>>>> 807a758950663c6b6e26c2cac7b24482510f36cc
