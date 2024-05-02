import subprocess

# List of words
words = ['instagram', 'cristiano', 'leomessi', 'selenagomez', 'kyliejenner', 'therock', 'arianagrande', 'kimkardashian', 'beyonce', 'khloekardashian', 'nike', 'kendalljenner', 'justinbieber', 'taylorswift', 'natgeo', 'virat', 'jlo', 'nickiminaj', 'kourtneykardash', 'neymarjr', 'mileycyrus', 'katyperry', 'zendaya', 'kevinhart4real', 'iamcardib', 'kingjames', 'realmadrid', 'ddlovato', 'badgalriri', 'champagnepapi', 'chrisbrownofficial', 'ellendegeneres', 'fcbarcelona', 'billieeilish', 'championsleague', 'k', 'gal_gadot', 'vindiesel', 'lalalalisa_m', 'nasa', 'priyankachopra', 'shakira', 'shraddhakapoor', 'narendramodi', 'dualipa', 'nba', 'davidbeckham', 'snoopdogg', 'jennierubyjane', 'aliaabhatt']

# Replace 'ishantmanderwal' with each word in the list and execute the command
for word in words:
    command = f"python instagram.py {word}"
    subprocess.run(command, shell=True)
