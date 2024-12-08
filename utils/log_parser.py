import os

def parse_logs(log_directory):
    print(f"Parsing logs in directory: {log_directory}...")
    parsed_data = []
    if not os.path.exists(log_directory):
        print("Log directory does not exist.")
        return parsed_data

    for file_name in os.listdir(log_directory):
        if file_name.endswith(".log"):
            file_path = os.path.join(log_directory, file_name)
            print(f"Parsing file: {file_name}")
            with open(file_path, "r") as file:
                for line in file:
                    if "ERROR" in line or "WARNING" in line:
                        parsed_data.append(line.strip())
    print(f"Log parsing complete. Found {len(parsed_data)} issues.")
    return parsed_data

def summarize_logs(parsed_data):
    print("Summarizing parsed logs...")
    summary = {
        "total_errors": sum(1 for line in parsed_data if "ERROR" in line),
        "total_warnings": sum(1 for line in parsed_data if "WARNING" in line),
    }
    print(f"Summary: {summary}")
    return summary
