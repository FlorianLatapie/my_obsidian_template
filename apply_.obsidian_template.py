import argparse
import shutil

parser = argparse.ArgumentParser(description='Apply the .obsidian folder to your obsidian vault')
parser.add_argument('-p', '--path', type=str, help='path to obsidian vault', default=None)
args = parser.parse_args()

destination_dir = args.path
if destination_dir is None:
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    Tk().withdraw()
    destination_dir = askdirectory(title='Select your Obsidian vault', initialdir = "./", mustexist=True)

destination_dir = destination_dir + ".obsidian/" if ".obsidian" not in destination_dir else destination_dir

source_dir = ".obsidian/"

try :
    if args.path is not None:
        print("importing from " + source_dir + " to " + destination_dir)
        input("Press Enter to continue...")
    
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    print("Done!")
except Exception as e:
    print('Directory not copied.')
    print(e)
