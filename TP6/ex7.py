import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def log_error(message):
    logging.error(message)

def read_file_logging(filename):
    livres = ["jump", "surrounded by idiots", "the unforgivable"]  
    try:
        if filename not in livres:
            raise FileNotFoundError
        return "The file " + str(filename) + " exists."
    except FileNotFoundError:
        error_message = f"The file '{filename}' does not exist."
        log_error(error_message)  
        return error_message

print(read_file_logging("jump"))  
print(read_file_logging("the rich dad poor dad"))  
