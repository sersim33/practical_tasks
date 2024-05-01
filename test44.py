
import re

def sanitize_file(source, output):
    with open(source, 'r') as fh:
        lines = fh.readlines()
    
    res = []     
    for line in lines:
        modified_line = re.sub(r'[0-9]', '', line)
        res.append(modified_line)
    
    with open(output, "w") as fh:
        fh.write(''.join(res))
    