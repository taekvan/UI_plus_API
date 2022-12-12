from mimesis import Person


def generate_random_person():
    person = Person()
    return {'name': person.first_name(),
            'surname': person.last_name(),
            'zip': person.identifier()
            }
