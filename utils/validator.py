import re

def validate_orderId(orderId):
    pattern = r'WSG\d+|wsg\d+|\d+\-\d+\-\d+'

    if re.match(pattern, orderId):
        return True
    else :
        return False
    
def validate_trackingId(trackingId):
    pattern = r'^[a-zA-Z0-9]{15}[0-9]$'
    
    if re.match(pattern, trackingId):
        return True
    else :
        return False