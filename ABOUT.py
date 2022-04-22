"""
******************************************************************************************************************
This GUI took me 3 or 4 days to create. It took me that long and struggled quite a bit because I am still pretty
new to programming and Python.

The close button wasn't going to be disabled at first, but I can't use .quit() because it closes both windows, I can't
use .destroy() because it gives me an error.

*******************************************************************************************************************

This is a Python tkinter GUI program that uses a local database to store contact information. Note: the GUI doesn't
create the database it only adds to one that is already on the local drive.

This first image is what the GUI looks like without any data inside it.

left frame submit button takes what you type into the entries and adds them to a local database and then the
entries get erased for the next entry and updates database in real time.

right frame submit button puts the contact information you select and puts it on the bottom of the GUI

When you select a contact and hit the edit button a new window pops up with entries with the data you selected
already in those entries. The close button is disabled, the submit button updates your changes in real time.

When you select a contact and click the delete button, that data is removed from the database and taken off the
list in real time.

"""