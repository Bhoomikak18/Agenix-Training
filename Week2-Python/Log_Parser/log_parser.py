import re
from database import Database  

# Defining the log line format 
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
        with open(self.file_path, 'r') as f:
            for line in f:
                parsed_line = self.parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
        return logs

    def process_logs(self):
        parsed_logs = self.parse_logs()
        # Insert 
        db = Database()  
        db.insert_log_data(parsed_logs)

if __name__ == "__main__":
    # Path to the Apache logs file
    log_file_path = "C:\\Users\\DELL\\Desktop\\Agenix\\Agenix-Training\\Week2-Python\\Log_Parser\\apache_logs.txt"

    log_parser = LogParser(log_file_path)
    log_parser.process_logs()
