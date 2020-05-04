
emails = {}
assert emails == {}, f"Expected 'emails' to be {{}} but got: {repr(emails)}"

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

assert emails == {
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected 'emails' to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth':'elizabeth@example.com'}} but got: {repr(emails)}"

del emails['craig']

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected 'emails' to be {{'ashley': 'ashley@example.com', 'elizabeth':'elizabeth@example.com'}} but got: {repr(emails)}"

emails['dalton'] = 'dalton@example.com'

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
    "dalton": "dalton@example.com",

}, f"Expected 'emails' to be {{'ashley': 'ashley@example.com', 'elizabeth':'elizabeth@example.com', 'dalton' : 'dalton@example.com}} but got: {repr(emails)}"

users = list(emails.keys())
print(f'Key is {users}')

email_list = list(emails.values())
print(f'Values are {email_list}')

pairs = list(emails.items())
print(pairs)
