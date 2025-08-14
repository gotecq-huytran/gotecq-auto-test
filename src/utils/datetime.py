from datetime import datetime

def dateGeneration(value: datetime, format: str = '%Y-%m-%d', ):
    date = datetime.now()
    if value:
        date = value
    
    return date.strftime(format)