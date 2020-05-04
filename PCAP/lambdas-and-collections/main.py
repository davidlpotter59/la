# import helpers as xyz
# from helpers import extract_lower as elow 
# from helpers import extract_upper as ehigh
# import helpers as h 
# import helpers 
from helpers import * 

# since __all__ = ['extract_upper'] is in helpers I need to import extract_lower
from helpers import extract_lower

# name = "David Potter"
# print(f"Lowercase letters: {helpers.extract_lower(name)}")
# print(f"Uppercase letters: {helpers.extract_upper(name)}")


def start():
    name = "David Potter"
    print(f"Lowercase letters: {extract_lower(name)}")
    print(f"Uppercase letters: {extract_upper(name)}")
    
# def start():
#     name = "David Potter"
#     print(f"Lowercase letters: {h.extract_lower(name)}")
#     print(f"Uppercase letters: {h.extract_upper(name)}")

# def start():
#     name = "David Potter"
#     print(f"Lowercase letters: {h.extract_lower(name)}")
#     print(f"Uppercase letters: {h.extract_upper(name)}")

if __name__ == "__main__":
    start()

# module search path
"""
3 main areas
1. from the directory that you are currently working in
2. PYTHONPATH=dirs/in/your/list
3. Python installation knows about
4. 3rd party packages (/usr/local/lib/python3.9/site-packages)

import sys
print(sys.path)
"""

import sys
print(sys.path)

# returns a list
my_path = [
        '/home/davep/python/la/PCAP/lambdas-and-collections', 
        '/usr/local/lib/python39.zip', 
        '/usr/local/lib/python3.9', 
        '/usr/local/lib/python3.9/lib-dynload', 
        '/usr/local/lib/python3.9/site-packages'
        ]
# it only searches through these paths only if there is not a built-in module by the
# name you are importing

for x in my_path:
    print(x)