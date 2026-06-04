""" Script to update an HTML template with serialized animal data. """

from animals_api import extract_animals_data

TARGET_HTML = "__REPLACE_ANIMALS_INFO__"


def return_animals_data():
    """ Takes input from the user and fetches animals information """
    animal_input = input("Enter a name of an animal: ")
    animals = extract_animals_data(animal_input)
    return animals, animal_input


def serialize_animal(animal):
    """ Serializes an animal object """
    output = ''
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += '<div class="card__text">'
    output += '<ul class="animal_list">'
    if "scientific_name" in animal["taxonomy"]:
        output += (f"<li class='animal_item'><strong>Scientific Name: "
                   f"</strong>{animal['taxonomy']['scientific_name']}</li>\n")
    if "diet" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Diet: </strong"
                   f">{animal['characteristics']['diet']}</li>\n")
    if animal['locations']:
        output += (f"<li class='animal_item'><strong>Location: </strong> "
                   f"{", ".join(animal["locations"])}</li>\n")
    if "type" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Type: </strong> "
                   f"{animal['characteristics']['type'].capitalize()}</li>\n")
    if "color" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Color: </strong>"
                   f"{animal['characteristics']['color']}</li>\n")
    if "skin_type" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Skin Type: </strong>"
                   f"{animal['characteristics']['skin_type']}</li>\n")
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def return_animals_output(animals, search_term):
    """ Returns the animal data """
    output = ""
    if not animals:
        output += (f"<h2>There are no animals containing '{search_term}'.</h2>")
    else:
        for animal in animals:
            output += serialize_animal(animal)
    return output


def load_html_template(file_path):
    """ Loads an HTML file """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def replace_html(html, animals):
    """ Replaces the HTML template with new animals data """
    return html.replace(TARGET_HTML, animals)


def write_animals_html(file_path, html):
    """ Writes the animal data into an HTML file """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)
    print("Success! Website was successfully generated to the file 'animals.html'.")


def main():
    """ Main function that handles the program logic """
    # load animals data
    data = return_animals_data()
    animals_data = data[0]
    user_input = data[1]

    # serialized animal data
    animals_output = return_animals_output(animals_data, user_input)

    # load html template
    html_orig = load_html_template('animals_template.html')

    # replace original html with new animals data
    updated_html = replace_html(html_orig, animals_output)

    # write final output
    write_animals_html('animals.html', updated_html)


if __name__ == "__main__":
    main()
