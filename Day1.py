import requests

headers = {
    "cookie" : "_ga=GA1.2.1313444699.1649263548; session=53616c7465645f5ff8514c580b1371a3cfc942bfd1f20b933829d22605d5aac19d8014fe91143f7c652f5d1cf47b2d4094f20db646530deb8a4ff5cd0c99f90e; _gid=GA1.2.1582783144.1654684564"
}

vstup = requests.get('https://adventofcode.com/2021/day/1/input', headers=headers).text.splitlines()
Numbers = [int(i) for i in vstup]
increase = 0

for i in range(0, len(Numbers)-3):
    sum_1 = sum(Numbers[i:i+3]) #sum_of_three = Numbers[i] + Numbers[i + 1] + Numbers[i + 2]
    sum_2 = sum(Numbers[i+1:i+4]) #sum_of_three_next = Numbers[i + 1] + Numbers[i + 2] + Numbers[i + 3
    if sum_1 < sum_2:
         increase += 1

print(increase)



