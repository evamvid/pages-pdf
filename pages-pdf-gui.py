from Tkinter import *
from tkFileDialog import *
import os.path
import shutil
import sys
import tempfile
from zipfile import ZipFile
import subprocess

class uiclass():
    def __init__(self,root):
        global w
        global quit
        global errlbl
        global restart
        global b
        global fbv
        global fv
        global qbt
        global cantOpen
        w = Label(root, text="Please choose a .pages file to convert.")
        quit = Label(root, text="Press 'q' to quit at any time")
        errlbl = Label(root, text="Error converting file.")
        restart = Button(root, text="Click here to restart", command=self.restart)
        b = Button(root, text="Browse", command=self.callback)
        fbv = Button(root, text="Click here to open PDF location", command=self.dirview)
        fv = Button(root, text="Click here to open PDF", command=self.fileview)
        qbt = Button(root, text="Click here to quit", command=self.qbt)
        frame = Frame(root, width=200)
        cantOpen = Label(root, text="This is not a valid .pages file")
        w.pack()
        b.pack()
        quit.pack()
        frame.pack()
    
    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        root.destroy()
    
    def dirview(self):
        if sys.platform=='win32':
            viewfile = filename + ".pdf"
            subprocess.Popen(r'explorer /select,'+ viewfile)
        elif sys.platform=='darwin':
            subprocess.Popen(['open', viewfile])
        else:
            try:
                subprocess.Popen(['xdg-open', viewfile])
            except OSError:
                cantOpen.pack()
        
    def callback(self):
        global y
        y = askopenfilename(parent=root, defaultextension=".pages")
        self.view_file(y)
        w.pack_forget()
        b.pack_forget()
        quit.pack_forget()
    
    def fileview(self):
        subprocess.Popen(filename + ".pdf", shell=True).wait()
    
    def qbt(self):
        root.destroy()
		
    def view_file(self,filepath):
        try:
            PREVIEW_PATH = 'QuickLook/Preview.pdf'  # archive member path
            #pages_file = raw_input('Enter the path to the .pages file in question: ')
            global pages_file
            pages_file = y
            pages_file = os.path.abspath(pages_file)
            global filename
            filename, file_extension = os.path.splitext(pages_file)
            if file_extension == ".pages":
                tempdir = tempfile.gettempdir()
                temp_filename = os.path.join(tempdir, PREVIEW_PATH)
                with ZipFile(pages_file, 'r') as zipfile:
                    zipfile.extract(PREVIEW_PATH, tempdir)
                if not os.path.isfile(temp_filename):  # extract failure?
                    errlbl = Label (root, text = "Unable to extract {} from {}.".format(PREVIEW_PATH, pages_file))
                    errlbl.pack()
                final_PDF = filename + '.pdf'
                shutil.copy2(temp_filename, final_PDF)  # copy and rename extracted file
                shutil.rmtree(os.path.join(tempdir, os.path.split(PREVIEW_PATH)[0])) # delete the temporary subdirectory created (along with pdf file in it)
                fv.pack()
                fbv.pack()
                qbt.pack()
                file_extension = ".pdf"
            else:
                global invalid
                invalid = Label(root, text='Sorry, that isn\'t a .pages file.')
                invalid.pack()
                qbt.pack()
                restart.pack()
        except:
            global invalid2
            invalid2 = Label(root, text='Sorry, that isn\'t a valid .pages file.')
            invalid2.pack()
            qbt.pack()
            restart.pack()
            
def quitfn(event=None):   
    root.destroy()
            
if __name__ == '__main__':
    root = Tk()
    uiclass(root)
    root.wm_title("Pages to PDF")
    root.bind("q", quitfn)
    root.mainloop()
    