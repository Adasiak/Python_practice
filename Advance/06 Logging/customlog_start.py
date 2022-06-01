# Demonstrate how to customize logging output
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()
import logging

extData = {
    "user": "adasiak@gmail.com"
}

# TODO: add another function to log from
def anotherFunction():
    logging.debug('Another function' , extra = extData)



def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr ="User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    datestring = "%m-%d-%y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt = datestring)

    logging.info("This is an info-level log message",  extra=extData)
    logging.warning("This is a warning-level message", extra=extData)


if __name__ == "__main__":
    main()
