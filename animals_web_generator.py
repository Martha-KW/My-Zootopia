import json

def load_data(file_path):
  """The function loads a json file with data about the animals."""
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animals_info(animals):
    """The function iterates over the animals_data.json, collects and prints the name
    and, if included in the json data, prints also the diet, the first location entry,
    and the type of the fox-animal."""
    for animal in animals:
        print("Name:", animal.get("name"))

        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            print("Diet:", characteristics.get("diet"))
        if "type" in characteristics:
            print("Type:", characteristics.get("type"))

        locations = animal.get("locations", [])
        if locations:
            print("Location:", locations[0])
        print()


def main():
    """Here is the main function that coordinates data collection and printing."""
animals_data = load_data('animals_data.json')
print_animals_info(animals_data)
if __name__ == "__main__":
    main()
