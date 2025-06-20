"""
wimbledon.py
Estimated time: 35 minutes
Actual time:  40 minutes
"""
def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    champion_to_wins = count_champions(data)
    countries = get_champion_countries(data)
    display_results(champion_to_wins, countries)

def read_data(filename):
    with open(filename,"r",encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        data = []
        for line in lines:
            data_parts = line.strip().split(",")
            data.append(data_parts)
        return data

def count_champions(data):
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins

def get_champion_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)

def display_results(champion_to_wins,countries):
    print("Wimbledon Champions:")
    for name, count in champion_to_wins.items():
        print(f"{name:20} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()