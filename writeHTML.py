import os
with open("mapTemplate.html", "r") as f:
	contents = f.read()

with open("webMap.html", "w") as f:
	f.write(contents.replace("placeholder", str(os.listdir("simgs"))))
