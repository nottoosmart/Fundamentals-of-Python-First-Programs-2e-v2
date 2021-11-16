# Put your code here
import os


def displayFiles(pathname):

    if os.path.isfile(pathname):
        print("File name:", pathname)

        if not pathname.endswith(".txt"):
            return

        file = open(pathname)

        for line in file:
            if not line.endswith("\n"):
                line += "\n"
            print(line, end="")

        file.close()

    elif os.path.isdir(pathname):

        print("Directory name:", pathname)

        if not pathname.endswith("//"):
            pathname += "/"
            
        for file in os.listdir(pathname):
            displayFiles(pathname + file)


if __name__ == "__main__":
    displayFiles(os.getcwd())
