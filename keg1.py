def convert_to_minutes(weeks):
    def partial_days(days):
        def partial_hours(hours):
            def partial_minutes(minutes):
                return (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes

            return partial_minutes

        return partial_hours

    return partial_days

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

results = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    conversion = convert_to_minutes(weeks)(days)(hours)(minutes)
    results.append(conversion)

for i, result in enumerate(results):
    print(f"OutputData = {result}")
