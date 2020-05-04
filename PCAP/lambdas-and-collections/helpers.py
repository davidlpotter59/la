"""
   this is my help module
"""

# module hiding
# when using the * extract_upper will only be available

__all__ = ['extract_upper']
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print(f"hello from helpers. Module name is {__name__}")