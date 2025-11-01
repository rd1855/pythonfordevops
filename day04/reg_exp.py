"""
    Regular Expressions Module for extracting Email IDs
"""

import re

text="""
        This alert service notify you about the latest updates.
        For more information, contact us at support@example.com
        and rdesai@gmail.com
    """

#print(dir(re))
#print(re.findall.__doc__)

list_of_emails = re.findall("[a-z0-9\.\-+]+@[a-z0-9\.\-+]+\.[a-z]",text)
print(list_of_emails)

