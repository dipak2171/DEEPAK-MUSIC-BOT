import os

thumbs = []
colors = ["white", "black", "red", "orange", "yellow", "green", "cyan", "azure", "blue", "violet", "magenta", "pink"]

for filename in os.listdir("./AnonX/assets"):
    if filename.endswith("png"):
        thumbs.append(filename[:-4])
