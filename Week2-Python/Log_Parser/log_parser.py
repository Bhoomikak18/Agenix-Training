import re
from database import insert_log_data  

# Define  
LOG_PATTERN = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/1\.[01]" (?P<status_code>\d+) (?P<bytes>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'

def parse_log_line(line):
    """Parse a single log line using the defined regular expression."""
    match = re.match(LOG_PATTERN, line)
    if match:
        return match.groupdict()
    return None

def parse_logs(file_path):
    """Parse the logs from the file and return a list of log entries."""
    logs = []
    with open(file_path, 'r') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if parsed_line:
                logs.append(parsed_line)

    return logs

if __name__ == "__main__":
    # Path to the Apache logs file
    log_file_path = "C:\\Users\\DELL\\Desktop\\Agenix\\Agenix-Training\\Week2-Python\\Log_Parser\\apache_logs.txt"


    # Parsing the logs
    parsed_logs = parse_logs(log_file_path)

    # Inserting the parsed logs into the database
    insert_log_data(parsed_logs)
