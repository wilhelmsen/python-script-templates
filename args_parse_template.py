#!/usr/bin/env python
# coding: utf-8
import logging
import os
import sys
import datetime

# Define the logger
LOG = logging.getLogger(__name__)

class ScriptException(Exception):
    pass

def main ():
    LOG.critical( "Look at me!! Look at me!!" )
    raise NotImplementedError

if __name__ == "__main__":

    # Uncomment if root privileges are required.
    # if os.geteuid() != 0:
    #    sys.exit("Must run as sudo!")

    try:
        import argparse
    except Exception, e:
        print ""
        print "Try running 'sudo apt-get install python-argparse' or 'sudo easy_install argparse'!!"
        print ""
        raise e

    def string2date( date_string ):
        # argparse.ArgumentTypeError()
        return datetime.datetime.strptime( date_string, '%Y-%m-%d' ).date()

    def directory( dir_path ):
        if not os.path.isdir( dir_path ):
            raise argparse.ArgumentTypeError( "'%s' does not exist. Please specify save directory!"%(dir_path))
        return dir_path

    parser = argparse.ArgumentParser( description='Some description. This script does this and that...' )
    parser.add_argument( 'required_date'
                         , type=string2date
                         , help='Required date...'
                         )
    parser.add_argument( '--dir'
                         , type=directory
                         , help='Some directory, that exists, if set (optional)...'
                         )
    parser.add_argument('--this-is-a-string-option'
                        , type=str
                        , help="Some string."
                        )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--debug', action='store_true', help="Output debugging information.")
    group.add_argument('-v', '--verbose', action='store_true', help="Output info.")
    parser.add_argument('--log-filename', type=str, help="File used to output logging information.")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig( filename=args.log_filename, level=logging.DEBUG )
    elif args.verbose:
        logging.basicConfig( filename=args.log_filename, level=logging.INFO )
    else:
        logging.basicConfig( filename=args.log_filename, level=logging.WARNING )

    # Output what is in the args variable.
    LOG.debug(args)

    main()
