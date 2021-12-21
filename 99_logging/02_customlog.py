# Customizing the logging return
import logging

"""
    basicFormat(
        format = format,
        dadefmt = date
    )

    💡 Most used specifiers

    %(asctime)s         Friendly format of date the message was logged
    %(filename)s        Name of the file where the message appeared
    %(funcName)s        Name of the function where the message appeared
    %(levelname)s       Text representing the message level (DEBUG, INFO, etc.)
    %(levelno)s         Numerical representation of message level
    %(lineno)s          Line of code where the message appeared
    %(message)s         The message to be logged itself
    %(module)s          Name of the module where the message appeared
"""

data = {"person": "jess"}

def other_log():
    logging.debug("This is a debug message", extra=data)

def main():
    # Set the logging level to debug and a file to save
    # the comeback. Also use custom formatting
    format = (
        "%(asctime)s: %(levelname)s: %(funcName)s "
        "Line:%(lineno)d Person:%(person)s %(message)s"
    )

    logging.basicConfig(
        filename="output.log",
        level=logging.DEBUG,
        format=format
    )

    logging.info("This is an info message", extra=data)
    logging.warning("This is a warning message", extra=data)
    other_log()

if __name__ == "__main__":
    main()