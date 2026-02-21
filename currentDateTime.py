from datetime import datetime

def get_current_datetime():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

print(get_current_datetime())