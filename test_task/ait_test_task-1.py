import itertools


"""
You have several managers ids 'user_ids' and a list of contacts.
Task: you need to apply managers (user_ids) to contacts (contacts[n]['manager_id'] one by one (round
robin).
You may use any python modules to succeed. Keep in mind, there can be any number of managers and
contacts.
"""


def round_robin(ids_list, contacts_list):
    user_id_generator = itertools.cycle(ids_list)
    for contact in contacts_list:
        contact['manager_id'] = next(user_id_generator)
    return contacts_list



if __name__ == '__main__':

    user_ids = [11, 12, 13, 14, 15]

    contacts = [
        {'name': 'John Doe', 'id': 1, 'manager_id': ''},
        {'name': 'Vasiya Pupkin', 'id': 2, 'manager_id': ''},
        {'name': 'John Pupkin', 'id': 3, 'manager_id': ''},
        {'name': 'Vasya Doe', 'id': 4, 'manager_id': ''},
        {'name': 'John Smith', 'id': 5, 'manager_id': ''},
        {'name': 'Homer Simpson', 'id': 6, 'manager_id': ''},
        {'name': 'Winnie the Pooh', 'id': 7, 'manager_id': ''},
        {'name': 'Bender Rodriguez', 'id': 8, 'manager_id': ''},
        {'name': 'Philip J. Fry', 'id': 9, 'manager_id': ''},
        {'name': 'Fox Mulder', 'id': 10, 'manager_id': ''},
        {'name': 'Parry Mason', 'id': 11, 'manager_id': ''}
    ]

    for i in round_robin(user_ids, contacts):
        print(i)
