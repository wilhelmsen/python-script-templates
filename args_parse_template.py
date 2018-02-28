#!/usr/bin/env python
# coding: utf-8
import logging
import os
import sys
import datetime

# Define the logger
LOG = logging.getLogger(__name__)


def main():
    LOG.critical("Look at me!! Look at me!!")


if __name__ == "__main__":
    # Uncomment if root privileges are required.
    # if os.geteuid() != 0:
    #    sys.exit("Must run as sudo!")

    try:
        import argparse
    except Exception as e:
        print("")
        print("Try running 'sudo apt-get install python-argparse' or")
        print("'sudo easy_install argparse'!!")
        print("")
        raise e

    def string2date(date_string):
        # argparse.ArgumentTypeError()
        return datetime.datetime.strptime(date_string,
                                          '%Y-%m-%d').date()

    def path(path):
        if not os.path.isdir(path) and not os.path.isfile(path):
            raise argparse.ArgumentTypeError(
                "'{}' does not exist.".format(path))
        return path

    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('required_date',
                        type=string2date,
                        help='Required date...')
    parser.add_argument('--dir',
                        type=path,
                        help='Some existing path, if set (optional)...')
    parser.add_argument('--this-is-a-string-option',
                        type=str,
                        help="Some string.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--debug', action='store_true',
                       help="Output debugging information.")
    group.add_argument('-v', '--verbose', action='store_true',
                       help="Output info.")
    parser.add_argument('--log-filename', type=str,
                        help="File used to output logging information.")
    args = parser.parse_args()

    if args.debug:
        log_level = logging.DEBUG
    elif args.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING

    log_format = " - ".join(["%(process)d",
                             "%(asctime)s",
                             "%(name)s",
                             "%(levelname)s",
                             "%(message)s"])

    logging.basicConfig(filename=args.log_filename,
                        level=log_level,
                        format=log_format)

    # Output what is in the args variable.
    LOG.debug(args)
    main()
