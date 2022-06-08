import requests

headers = {
    "cookie" : "__ga=GA1.2.1313444699.1649263548; session=53616c7465645f5ff8514c580b1371a3cfc942bfd1f20b933829d22605d5aac19d8014fe91143f7c652f5d1cf47b2d4094f20db646530deb8a4ff5cd0c99f90e; _gid=GA1.2.1582783144.1654684564; _gat=1"
}

vstup = requests.get('https://adventofcode.com/2021/day/2/input', headers=headers).text.split("\n")[:-1]

print(vstup)
horizontal_position = 0
vertical_position = 0
aim = 0

for line in vstup:
    direction,length = line.split(" ")
    if direction == "forward":
        if aim > 0:
            horizontal_position += int(length)
            vertical_position += int(length) * aim
        if aim == 0:
            horizontal_position += int(length)
    elif direction == "up":
        aim -= int(length)
    elif direction == "down":
        aim += int(length)

print(horizontal_position * vertical_position)
