# Parses user's arguments and calls functions accordingly.
def main(args):
    import datetime
    import os
    import pathlib

    # dates is a list that stores date entries read from date_file. Changes
    # are made to dates (i.e. dates are removed) and these changes are
    # applied to the date_file by calling the update_date_file() function.
    dates = None

    # The date_file contains date entries written in plain text. These entries
    # consist of an iso-formatted date and an optional date_name. This file
    # can be found in the home directory as .date_list.
    date_file = None

    # Dates are stored in "YYYY-MM-DD" format. This function takes such a
    # string and turns in into and instance of datetime.date.
    def make_datetime_date(date_string):
        date_components = [
            int(date_component) for date_component in date_string.split("-")
        ]
        date = datetime.date(date_components[0], date_components[1],
                             date_components[2])
        return date

    # Adds a date and its name to the date_file
    def add_date(date, name):
        if name == None:
            name = ""
        date_file.write(date.isoformat() + " " + name + "\n")
        print("Date added.")

    # Removes a date from the date_file
    def remove_date(identifier):
        removed_date = False
        for entry in dates:
            split_entry = entry.split()
            date, name = split_entry[0], split_entry[
                1] if len(split_entry) > 1 else None

            # The identifier can match either the date or its name
            if identifier == date or identifier == name:
                dates.remove(entry)
                removed_date = True
                break

        if removed_date:
            print("Date removed")
            # date_file must be updated (rewritten) now that dates has
            # been changed
            update_date_file()
        else:
            print("Date not found")

    # Rewrites the date_file using the entries stored in dates
    def update_date_file():
        date_file.seek(0)  # File was already read, must seek to zero
        date_file.truncate()  # Delete everything in the file
        for entry in dates:
            date_file.write(entry)

    # Determines whether the user is wanting to remove or add a date
    # Handles getting the name and date from the args passed
    def modify_date_file(command, args):
        date, name = None, None
        if type(args) == list:
            date, name = args[0], args[1] if len(args) > 1 else None
        else:
            date = args
            name = None

        if command == "add_date":
            try:
                datetime_date = make_datetime_date(date)
                add_date(datetime_date, name)
            except (ValueError, IndexError):
                print(
                    "Incorrect date format for the first argument. Please use YYYY-MM-DD."
                )
        elif command == "remove_date":
            try:
                datetime_date = make_datetime_date(date)
                remove_date(datetime_date.isoformat())
            except (ValueError, IndexError):
                remove_date(
                    date
                )  # Because date cannot be formatted to a datetime date, it is assumed to be a name

    def howmuchtime():
        if len(dates) > 0:
            today = datetime.date.today()
            expired_dates = []

            # The time remaining between today and each stored date is
            # calculated and outputted.
            for entry in dates:
                split_entry = entry.split()
                date, name = split_entry[0], split_entry[
                    1] if len(split_entry) > 1 else None

                time_remaining = make_datetime_date(date) - today
                name_string = ((str(name) + " ") if name else "")

                # If time_remaining is negative, meaning the date has passed,
                # it will fail the if statement and the corresponding 
                # entry will be removed. 
                if time_remaining == abs(time_remaining):
                    print(name_string + date + ": " +
                          str(time_remaining.days) + " days (" +
                          str(time_remaining.days * 24) + " hours) remaining.")
                else:
                    expired_dates.append((date, name_string, entry))

            removed_date = False
            for date, name_string, entry in expired_dates:
                removed_date = True
                print(name_string + date + " has passed. Date removed.")
                dates.remove(entry)

            if removed_date is True:
                update_date_file()

        else:
            print("No dates tracked. Get help with 'hmt -h'")

    home_dir = str(pathlib.Path.home())

    # The date_list is opened and its contents are stored in the dates array
    # for accessibility.
    with open(os.path.join(home_dir, ".date_list"), "a+") as date_file:
        date_file.seek(0)
        dates = [date for date in date_file]
        for key, value in args.items():
            if value:
                modify_date_file(key, value)
                break
        else:
            howmuchtime()


def cli():
    import argparse

    # Hack to get the usage for --add-date to display correctly.
    class PrintCustomHelp(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            import re
            h = cli.format_help()
            print(re.sub('\[name ...\]', '[name]', h))
            parser.exit()

    cli = argparse.ArgumentParser(
        description="Countdown to a date.", add_help=False)
    date_commands = cli.add_mutually_exclusive_group()
    date_commands.add_argument(
        "-a",
        "--add-date",
        nargs="+",
        metavar=("date", "name"),
        help="Add date in YYYY-MM-DD format (with an optional name) for counting down to"
    )
    date_commands.add_argument(
        "-r",
        "--remove-date",
        metavar="date/name",
        help="Remove a currently tracked date by specifying the date or its name")
    date_commands.add_argument(
        "-h",
        "--help",
        nargs=0,
        action=PrintCustomHelp,
        help="Show this help message and exit")

    args = vars(cli.parse_args())

    # Add_date can only take one or two arguments.
    if args["add_date"] is not None and len(args["add_date"]) > 2:
        print(
            "--add-date takes at most two arguments: a date and an optional name"
        )
    else:
        main(args)
