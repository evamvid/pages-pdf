[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=evamvid&url=github.com/evamvid/pages-pdf&title=pages-pdf&language=&tags=github&category=software) 

pages-pdf
=========

A simple python script that converts a .pages document into a PDF. Command-line version (executable without the Python shell), and executables coming soon! (hopefully)

The scripts _should_ be cross-platform but they have only been tested on Windows.

The Scripts
===========
* pages-pdf-console.py is the working console version.
* pages-pdf-gui.py is the working GUI version. To make it run without a console in Windows.
* pages-pdf-old.py (in the legacy folder) is the old script, that I wrote all on my lonesome before going to SO for help (it turns out that that the `ZipFile` module I was trying to use didn't have the functionality I needed). It is here for historical/legacy purposes, and to prove how much I needed the help I got from SO. Note that this script is not functional.

Attributions/Acknowledgements
=============================
If not for the help of StackOverflow users [Martineau](http://stackoverflow.com/users/355230/martineau), [Ruben Bermudez](http://stackoverflow.com/users/2397017/ruben-bermudez), [J.F. Sebastian](http://stackoverflow.com/users/4279/j-f-sebastian), and [shaktimaan](http://stackoverflow.com/users/2276527/shaktimaan), I probably would not have the program running right now.
You can see the individual questions where they completely overhauled my code until it was barely recognizable as mine [here](http://stackoverflow.com/questions/22161088/how-to-extract-a-file-within-a-folder-within-a-zip-in-python), [here](http://stackoverflow.com/questions/22213600/python-tkinter-file-dialog), [here](http://stackoverflow.com/questions/22215388/how-to-suppress-windows-file-handling-with-python), and [here](http://stackoverflow.com/questions/22214766/running-mainloop-in-its-own-thread-or-process)
