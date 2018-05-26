howmuchtime
===========

Countdown to a date.

This package is a simple command line app for counting down (in days) to
a date. Call ``hmt`` at any time to see the days remaining for all added
dates.

For example:

::

   $ hmt -a 2018-09-20
   Date added.
   $ hmt
   2018-09-20: 118 days (2832 hours) remaining.

Installation
------------

Install with:

::

   $ pip install howmuchtime

*If hmt is not installed as a script, try re-installing with* ``sudo pip install howmuchtime``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
-----

Add a date to countdown to with:

::

   $ hmt -a <YYYY-MM-DD>

If you no longer want the countdown to a date, remove it with:

::

   $ hmt -r <YYYY-MM-DD>

Finally, to view the countdown, just call hmt:

::

   $ hmt

Additional Help
---------------

::

   usage: hmt [-h] [-a date | -r date]

   Countdown to a date.

   optional arguments:
     -h, --help  show this help message and exit
     -a date     Add date in YYYY-MM-DD formate for counting down to.
     -r date     Removed a currently tracked date.
