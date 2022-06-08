import requests

headers = {
    "cookie" : "_ga=GA1.2.1313444699.1649263548; session=53616c7465645f5ff8514c580b1371a3cfc942bfd1f20b933829d22605d5aac19d8014fe91143f7c652f5d1cf47b2d4094f20db646530deb8a4ff5cd0c99f90e; _gid=GA1.2.1582783144.1654684564"
}

vstup = requests.get('https://adventofcode.com/2021/day/3/input', headers=headers).text.split("\n")[:-1]

oxygen_generator_rating = []
CO2_scrubber_rating = []

for line in vstup:
    oxygen_generator_rating.append([int(a) for a in str(line)])
    CO2_scrubber_rating.append([int(a) for a in str(line)])

for stlpec in range(len(oxygen_generator_rating[0])):
    count = 0
    for riadok in range(len(oxygen_generator_rating)):
        count += oxygen_generator_rating[riadok][stlpec]
    if len(CO2_scrubber_rating) <= 1:
        break
    else:
        if count >= (len(oxygen_generator_rating) / 2):
            most_common_bit = 1
        else:
            most_common_bit = 0
        oxygen_generator_rating = [x for x in oxygen_generator_rating if x[stlpec] == most_common_bit ]

for stlpec in range(len(CO2_scrubber_rating[0])):
    count = 0
    for riadok in range(len(CO2_scrubber_rating)):
        count += CO2_scrubber_rating[riadok][stlpec]
    if len(CO2_scrubber_rating) <= 1:
        break
    else:
        if count >= (len(CO2_scrubber_rating) / 2):
            least_common_bit = 0
        else:
            least_common_bit = 1
    CO2_scrubber_rating = [x for x in CO2_scrubber_rating if x[stlpec] == least_common_bit ]


print((int("".join(map(str, oxygen_generator_rating[0])), 2)) * int("".join(map(str, CO2_scrubber_rating[0])),2))
