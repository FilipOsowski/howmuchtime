# howmuchtime
Countdown to a date.

This package is a simple command line app for counting down (in days) to a date. Call ``hmt`` at any time to see the days remaining for all added dates.

For example:

```
$ hmt -a 2018-09-20 Birthday
Date added.
$ hmt
Birthday 2018-09-20: 118 days (2832 hours) remaining.
```
## Installation
Install with:
```
$ pip install howmuchtime
```
#### _If hmt is not installed as a script, try re-installing with_ ``sudo pip install howmuchtime``
## Usage
Add a date to countdown to with:
```
$ hmt -a <YYYY-MM-DD> <optional name>
```
If you no longer want the countdown to a date, remove it with:
```
$ hmt -r <YYYY-MM-DD>
$ # or using a name
$ hmt -r <name>
```
Finally, to view the countdown, just call hmt:
```
$ hmt
```
## Additional Help
```
usage: hmt [-a date [name] | -r date/name | -h]

Countdown to a date.

optional arguments:
  -a date [name], --add-date date [name]
                        Add date in YYYY-MM-DD format (with an optional name)
                        for counting down to
  -r date/name, --remove-date date/name
                        Remove a currently tracked date by specifying the date
                        or its name
  -h, --help            Show this help message and exit
```
