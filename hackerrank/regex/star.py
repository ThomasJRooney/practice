Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())