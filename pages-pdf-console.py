import os.path
import shutil
import sys
import tempfile
from zipfile import ZipFile
import subprocess

def view_file(filepath):
	subprocess.Popen(filepath, shell=True).wait()

PREVIEW_PATH = 'QuickLook/Preview.pdf'  # archive member path
pages_file = raw_input('Enter the path to the .pages file in question: ')
#pages_file = r'C:\Stack Overflow\extract_test.pages'  # hardcode for testing
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
    view_file(final_PDF) # see Bonus below
else:
    sys.exit('Sorry, that isn\'t a .pages file.')