import re
log_file_path = "C:/Users/Syed Ibrahim/Downloads/log_test.csv"
latency_pattern = r'\b\d+\.\d+$'
with open(log_file_path, 'r') as file:
    for line in file:
        match = re.search(latency_pattern, line)
        if match:
            print(match.group())