# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        # Use a regex to find all valid email addresses
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        
        # Find all email addresses matching the pattern
        emails = re.findall(email_pattern, self.email_string)
        
        # Remove duplicates by converting to a set and back to a list, then sort
        unique_emails = sorted(list(set(emails)))
        
        return unique_emails
