# Using the logging module

# Use the built-in logging module
import logging


def main():
    # Use basicConfig to configure your logging
    # Reminder: this part is only performed once, calls
    # subsequent will have no effect
    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log")

    # Testing each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is an information message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    # Use strings to format the log
    logging.info("Here we have a variable {} and an int: {}".format("string", 10))


if __name__ == "__main__":
    main()