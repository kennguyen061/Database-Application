
CPSC 4620 PROJECT 4
-------------------
Joey Binz
Kenny Nguyen

4/19/2021
-------------------

Driver file: p4.py

-------------------

This project contains the source code for a python application that interfaces with
    the Clemson Computer Solutions database that has been designed this semester.

The application is launched via p4.py (with the command p4.py) and the source code
    is broken up into two main sections, db & GUI.

GUI
----
    The GUI package contains all of the tkinter code for the GUI (excluding the
        first menu which is contained in p4.py). This is broken up into 

            insertGUI.py - for the insert menus

            reportsGUI.py - for the report menus

            transactionsGUI.py - for the transaction menus

        insertGUI is the most complex of the 3, and contains the most menus.

db
----
    the db package contains all (except the code in p4.py) of the code that
        interacts with the database. The db package also contains a few utility
        functions as well. It is divided into three files

            database.py - contains the large majority of selects & inserts

            dates.py - contains utility functions for converting dates to SQL format

            seed.py - contains the code for inserting the seed data into the database

extra
------
    The extra folder includes files that were used for debugging/testing along
        development & can largely be ignored. One file of note:

            debug.py - when run it resets the databse to a fresh schema