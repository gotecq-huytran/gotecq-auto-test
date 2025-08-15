from datetime import datetime

def dateGeneration(value: datetime = None, format: str = '%m/%d/%Y'):
    date = datetime.now()
    if value:
        date = value
    
    return date.strftime(format)