import xml.etree.ElementTree as eT


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = eT.iterparse(filename, ('start', 'end'))

    # Skip root element
    next(doc)

    tag_stack = []
    elem_stack = []

    for event, elem in doc:

        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)

        elif event == 'end':
            if tag_stack == path_parts:
                yield elem

            try:
                tag_stack.pop()
                elem_stack.pop()

            except IndexError:
                pass


governments = []
countries = parse_and_remove(r"C:\DB\mondial-3.0.xml", "country")

for country in countries:
    # get the attribute name, split it into list and get its length
    words_in_country_name = len(str(country.attrib['name']).split(" "))
    government = country.attrib['government']
    # if the government does not exist in the list and amount of words
    # in country name is equal to 2, then add the government to the list
    if government not in governments and words_in_country_name == 2:
        governments.append(government)

# form a string with elements of government list, separated by comma
result = ', '.join(governments)

print(result)

