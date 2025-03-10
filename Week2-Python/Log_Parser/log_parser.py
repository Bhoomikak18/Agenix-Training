import re
import argparse
import logging
from database import Database  

# Define  
LOG_PATTERN = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/1\.[01]" (?P<status_code>\d+) (?P<bytes>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'

class LogParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_log_line(self, line):
        match = re.match(LOG_PATTERN, line)
        if match:
            return match.groupdict()
        return None

    def parse_logs(self):
        logs = []
        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    parsed_line = self.parse_log_line(line)
                    if parsed_line:
                        logs.append(parsed_line)
            logging.info(f"Successfully parsed {len(logs)} log entries.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
        except Exception as e:
            logging.error(f"Error while reading file: {e}")
        return logs

    def process_logs(self):
        parsed_logs = self.parse_logs()
        if parsed_logs:
            db = Database()
            db.insert_log_data(parsed_logs)
            logging.info("Logs successfully inserted into the database.")
        else:
            logging.warning("No logs were parsed. Nothing to insert.")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    parser = argparse.ArgumentParser(description="Apache Log Parser")
    parser.add_argument("log_file", type=str, help="Path to the Apache log file")
    args = parser.parse_args()

    # Initialize and process logs
    log_parser = LogParser(args.log_file)
    log_parser.process_logs()
