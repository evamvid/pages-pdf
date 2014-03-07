[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=evamvid&url=github.com/evamvid/pages-pdf&title=pages-pdf&language=&tags=github&category=software) 

pages-pdf
=========

A simple python script that converts a .pages document into a PDF. Command-line version (executable without the Python shell), and executables coming soon! (hopefully)

The scripts _should_ be cross-platform but they have only been tested on Windows.

The Scripts
===========
* pages-pdf.py is the working console version.
* pages-pdf-gui.py is the working GUI version. To make it run without a console in Windows.
* pages-pdf.py is the old script, that I wrote all on my lonesome before going to SO for help (it turns out that that the `ZipFile` module I was trying to use didn't have the functionality I needed). It is here for historical/legacy purposes, and to prove how much I needed the help I got from SO.
* py2.7install.bat is a Windows shell script that will install [Chocolatey](https://chocolatey.org/) and then [Python 2.7](http://www.python.org/download/releases/2.7.6/)(2.7.6, the most current version of 2.7) in the main `C:\` drive. 

Attributions/Acknowledgements
=============================
If not for the help of StackOverflow users [Martineau](http://stackoverflow.com/users/355230/martineau), [Ruben Bermudez](http://stackoverflow.com/users/2397017/ruben-bermudez), [J.F. Sebastian](http://stackoverflow.com/users/4279/j-f-sebastian), and [shaktimaan](http://stackoverflow.com/users/2276527/shaktimaan), I probably would not have the program running right now.
You can see the individual questions where they completely overhauled my code until it was barely recognizable as mine [here](), [here](), and [here]().
