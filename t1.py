import requests
import json
import random

n = int(input("Enter a count of character: "))


def get_random_character(n):

    for i in range(n):
        magic = random.randint(100, 1000)
        resp = requests.get("https://www.anapioficeandfire.com/api/characters/" + str(magic))
        data = resp.text
        parse = json.loads(data)
        name = parse["name"]
        played = parse["playedBy"]
        actor = ''.join(played)
        if not actor:
            actor = '-'
        print(name, actor)


get_random_character(n)
