COLOURS_TO_HEX = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb",
                 "AntiqueWhite2": "#eedfcc"}

lower_colour_dict = {name.lower(): name for name in COLOURS_TO_HEX}
input_colour = input("Enter colour name: ")
while input_colour != "":
    name_list = input_colour.split(",")
    for colour in name_list:
        colour = colour.strip().lower()
        try:
            original_name = lower_colour_dict[colour]
            hex_code = COLOURS_TO_HEX[original_name]
            print(f"{original_name} is {hex_code}")
        except KeyError:
            print(f"{colour} is Invalid colour name")
    input_colour = input("Enter colour name: ")