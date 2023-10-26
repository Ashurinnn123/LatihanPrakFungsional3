data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

integer_values = []

for item in data:
    values = filter(str.isdigit, item)
    integer_values.append(" ".join(values))

print(integer_values)
