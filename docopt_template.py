#!/usr/bin/env python
"""Usage:
    docopt_template.py command1 [options] <arg1> <arg2> ARG3 [--verbose|--debug]
    docopt_template.py command2 [options] <arg1> ARG2 <arg3> [--verbose|--debug]

Options:
    -a=OPTION, --option1=OPTION       En eller anden option 1.
                                      Lidt mere her. [default: 23]
    -b, --option2=option2             En eller anden option 2.
    -d, --debug                       Output a lot of info..
    -v, --verbose                     Output less less info.
    --log-filename=logfilename        Name of the log file.
"""
import logging
import docopt
# Define the logger
LOG = logging.getLogger(__name__)

args = docopt.docopt(__doc__, version="1.0")
if args["--debug"]:
    logging.basicConfig( filename=args["--log-filename"], level=logging.DEBUG )
elif args["--verbose"]:
    logging.basicConfig( filename=args["--log-filename"], level=logging.INFO )
else:
    logging.basicConfig( filename=args["--log-filename"], level=logging.WARNING )
LOG.info(args)

def main():
    LOG.debug("Se mig! Se mig!")


if __name__ == "__main__":
    main()
