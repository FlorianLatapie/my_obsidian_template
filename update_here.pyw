import argparse
import shutil
import os

parser = argparse.ArgumentParser(description='Import a file into Obsidian')
parser.add_argument("-p", "--path", type=str, help="path to .obsidian folder", default=None)
args = parser.parse_args()

source_dir = args.path
if source_dir is None:
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    Tk().withdraw()
    source_dir = askdirectory(title='Select your Obsidian vault', initialdir = "./", mustexist=True)

if (".obsidian" not in source_dir) and (not os.path.exists(source_dir+"/.obsidian")):
    print("Error: source directory does not contain .obsidian folder")
    exit(1)

source_dir = source_dir + "/.obsidian/" if ".obsidian" not in source_dir else source_dir

destination_dir = ".obsidian/"

try :
    if args.path is not None:
        print("importing from " + source_dir + " to my_obsidian_template/" + destination_dir)
        input("Press Enter to continue...")

    shutil.rmtree(destination_dir, ignore_errors=True)

    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

    os.remove(destination_dir+"workspace.json")
    os.remove(destination_dir+"workspace-mobile.json")
    os.remove(destination_dir+"graph.json")
    
    if args.path is not None:
        print("Done!")
    else:
        # tkinter messagebox "Done!"
        from tkinter import Tk
        from tkinter import messagebox
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Done!", "This repo has been updated, you can now close this window and commit the changes.")
except Exception as e:
    print('Directory not copied.')
    print(e)
