import logging 

logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event_type, message):
    logging.info(message) 
    