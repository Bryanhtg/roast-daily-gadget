import os

os.makedirs("/output", exist_ok=True)
roast = 'My office printer refuses to print a black-and-white tax form because it\'s "low on cyan," like a bodybuilder refusing to lift weights until he gets a pedicure.'
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(roast)
