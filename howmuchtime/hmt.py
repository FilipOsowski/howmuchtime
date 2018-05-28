# Parses user's arguments and calls functions accordingly.
def main(args):
    import datetime
    import os
    import pathlib

    # Since dates are stored in "YYYY-MM-DD" format, this function takes such a
    # string and turns in into and instance of datetime.date.
    def make_datetime_date(date_string):
        date_components = [
            int(date_component) for date_component in date_string.split("-")
        ]
        date = datetime.date(date_components[0], date_components[1],
                             date_components[2])
        return date

    # Adds or removes a date from/to the date_list.
    def modify_date_list(command, date):

        # Basic check to make sure the user's date can be used.
        try:
            date = make_datetime_date(date)
        except (ValueError, IndexError):
            print("Incorrect date format. Please use YYYY-MM-DD.")
        else:
            if command == "a":
                date_list.write(date.isoformat() + "\n")
                print("Date added.")

            else:

                # Check to make sure the date specified is in the date_list.
                try:
                    dates.remove(date.isoformat() + "\n")
                except ValueError:
                    print("Date not found.")

                # After a date is removed, date_list is rewritten using the
                # dates array.
                else:
                    date_list.seek(0)
                    date_list.truncate()
                    for remaining_date in dates:
                        date_list.write(remaining_date)
                    print("Date removed.")

    def howmuchtime():
        if len(dates) > 0:
            today = datetime.date.today()
            expired_dates = []

            # The time remaining between today and each stored date is calculated
            # and outputted.
            for date in dates:
                time_remaining = make_datetime_date(date) - today
                if time_remaining == abs(time_remaining):
                    print(
                        date[:-1] + ": " + str(time_remaining.days) + " days ("
                        + str(time_remaining.days * 24) + " hours) remaining.")

                # If a date has passed, the user is notified of its removal.
                else:
                    expired_dates.append(date[:-1])

            for date in expired_dates:
                print(date + " has passed.", end=' ')
                modify_date_list("r", date)
        else:
            print("No dates tracked. Get help with 'hmt -h'")

    # my_loc = os.path.dirname(os.path.abspath(__file__))
    home_dir = str(pathlib.Path.home())

    # The date_list is opened and its contents are stored in the dates array
    # for accessibility.
    with open(os.path.join(home_dir, ".date_list"), "a+") as date_list:
        date_list.seek(0)
        dates = [date for date in date_list]
        for key, value in args.items():
            if value:
                modify_date_list(key, value)
                break
        else:
            howmuchtime()


def cli():
    import argparse

    cli = argparse.ArgumentParser(description="Countdown to a date.")
    date_commands = cli.add_mutually_exclusive_group()
    date_commands.add_argument(
        "-a",
        metavar="date",
        help="Add date in YYYY-MM-DD formate for counting down to.")
    date_commands.add_argument(
        "-r", metavar="date", help="Removed a currently tracked date.")

    args = cli.parse_args()
    main(vars(args))
