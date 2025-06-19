"""
wimbledon.py
Estimated time: 35 minutes
Actual time:   minutes
"""
def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    print(data)
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
def count_champions():
    return

def get_champion_countries():
    return

def display_results():
    return

main()