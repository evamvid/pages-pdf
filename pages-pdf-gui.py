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
        global b
        b = Button(root, text="Browse", command=self.callback)
        global w
        w = Label(root, text="Please choose a .pages file to convert.")
        global quit
        quit = Label(root, text="Press 'q' to quit at any time")
        w.pack()
        b.pack()
        quit.pack()
        
        
    #def quitfn(event):
    #    frame.focus_set()
    #    print ("hello")
    #    window.destroy()

    def callback(self):
        global y
        y = askopenfilename(parent=root, defaultextension=".pages")
        self.view_file(y)
        w.pack_forget()
        b.pack_forget()
		
    def view_file(self,filepath):

        PREVIEW_PATH = 'QuickLook/Preview.pdf'  # archive member path
        #pages_file = raw_input('Enter the path to the .pages file in question: ')
        pages_file = y
        pages_file = os.path.abspath(pages_file)
        filename, file_extension = os.path.splitext(pages_file)
        if file_extension == ".pages":
            tempdir = tempfile.gettempdir()
            temp_filename = os.path.join(tempdir, PREVIEW_PATH)
            with ZipFile(pages_file, 'r') as zipfile:
                zipfile.extract(PREVIEW_PATH, tempdir)
            if not os.path.isfile(temp_filename):  # extract failure?
                sys.exit('unable to extract {} from {}'.format(PREVIEW_PATH, pages_file))
            final_PDF = filename + '.pdf'
            shutil.copy2(temp_filename, final_PDF)  # copy and rename extracted file
            # delete the temporary subdirectory created (along with pdf file in it)
            shutil.rmtree(os.path.join(tempdir, os.path.split(PREVIEW_PATH)[0]))
            print('Check out the PDF! It\'s located at "{}".'.format(final_PDF))
            l2.pack_forget()
            subprocess.Popen(filename + ".pdf", shell=True).wait()
            file_extension = ".pdf"
        else:
            sys.exit('Sorry, that isn\'t a .pages file.')

def quitfn(event=None):   
    root.destroy()
            
if __name__ == '__main__':
    root = Tk()
    uiclass(root)
    root.wm_title("Pages to PDF")
    root.bind("q", quitfn)
    root.mainloop()
    