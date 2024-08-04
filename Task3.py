from collections import Counter
import sys

# Supported log levels
LOG_LEVELS = ["ERROR", "WARNING", "INFO", "DEBUG"]

def parse_log_line(line: str) -> dict:
    """
    Parses a log line and returns a dictionary with the following keys:
    "date", "time", "level", "message"

    Parameters:
        line (str): A string representing a log line.

    Returns:
        dict: A dictionary containing the parsed log data.   
    """
    date, time, log_level, message = line.split(" ", 3)
    return {"date": date, "time": time, "level": log_level, "message": message}


def load_logs(file_path: str) -> list:
    """
    Loads log data from a file and returns a list of dictionaries.

    Parameters:
        file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries representing the log data.    
    """
    logs = []
    with open(file_path, "r", encoding="utf-8") as f:
        [logs.append(parse_log_line(line.strip())) for line in f]

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters a list of log dictionaries by log level.

    Parameters:
        logs (list): A list of log dictionaries.
        level (str): The log level to filter by.

    Returns:
        list: A list of log dictionaries with the specified log level.    
    """
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of logs by log level.

    Parameters:
        logs (list): A list of log dictionaries.

    Returns:
        dict: A dictionary containing the count of logs by log level.
    """
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict):
    """
    Displays the count of logs by log level.

    Parameters:
        counts (dict): A dictionary containing the count of logs by log level.
    """
    TOTAL_WIDTH = 43
    L_WIDTH = 30
    R_WIDTH = 10
    print('-' * TOTAL_WIDTH)

    print('|' + "LOG LEVELS".center(L_WIDTH) + '|' + 'COUNT'.center(R_WIDTH) + '|')
    print('-' * TOTAL_WIDTH)

    for level, count in counts.items():
        print('|' + f'{level}'.ljust(L_WIDTH) + '|' + f'{count}'.center(R_WIDTH) + '|')
    print('-' * TOTAL_WIDTH)


def print_logs_by_level(logs: list, level: str):
    """
    Prints the logs with the specified log level.

    Parameters:
        logs (list): A list of log dictionaries.
        level (str): The log level to filter by.
    
    Raises:
        ValueError: If the specified log level is not supported.
    """
    level_upper = level.upper()
    if level_upper not in LOG_LEVELS:
        raise ValueError(f"Unsupported log level: {level_upper}")

    print(f"\nLogs with level: '{level_upper}'")
    for log in filter_logs_by_level(logs, level_upper):
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    try:
        if len(sys.argv) < 2 or len(sys.argv) > 3:
            raise ValueError("Usage: python Task3.py <log_file> [log_level]")

        logs = load_logs(sys.argv[1])
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if len(sys.argv) == 3:
            print_logs_by_level(logs, sys.argv[2])

    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")


if __name__ == "__main__":
    main()
