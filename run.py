import json
k = open("data.json", "a")
for i in open("spam.txt", encoding="UTF-8").readlines():
    k.write(json.dumps(dict(
        text=i.strip(),
        label="spam"
        )))
    k.write("\n")
for i in open("regular.txt", encoding="UTF-8").readlines():
    k.write(json.dumps(dict(
        text=i.strip(),
        label="regular"
        )))
    k.write("\n")
k.close()