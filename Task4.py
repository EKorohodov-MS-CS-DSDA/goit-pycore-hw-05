from functools import wraps
from typing import Callable

def input_error(func: Callable) -> Callable:
    """
    A decorator wrapper to handle input errors in the given function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"[{func.__name__}] {e}"
        except IndexError:
            return f"[{func.__name__}] {e}"
        except KeyError:
            return f"[{func.__name__}] {e}"
    return wrapper

@input_error
def add_contact(tokens: list, contacts: dict) -> str:
    """
    Adds a contact to the given dictionary of contacts.
    Parameters:
        tokens (list): A list of strings representing the new contact information.
        contacts (dict): A dictionary containing the contacts.
    Returns:
        str: A string indicating the result of the operation.
    Raises:
        ValueError: If the number of tokens is less than 2 or if the name already exists 
        in the contacts dictionary.
    """
    if len(tokens) < 2:
        raise ValueError("Not enough arguments. Input: add <name> <phone>")

    data = {"name": ' '.join(tokens[:-1]), "phone": tokens[-1]}
    if data["name"] in contacts:
        raise ValueError("Name already exist")
    else:
        contacts[data["name"]] = data["phone"]

    return f"Added {data['name']} with phone {data['phone']}"


@input_error
def change_contact(tokens: list, contacts: dict) -> str:
    """
    Change the contact information for a given name in the contacts dictionary.
    Args:
        tokens (list): A list of strings representing the contact information. 
            The first element is the name and the last element is the phone number.
        contacts (dict): A dictionary containing the contacts.
    Returns:
        str: A string indicating the result of the operation.
    Raises:
        ValueError: If the number of tokens is less than 2 or if the name does not exist 
        in the contacts dictionary.
    """
    if len(tokens) < 2:
        raise ValueError("Not enough arguments. Input: change <name> <phone>")

    data = {"name": ' '.join(tokens[:-1]), "phone": tokens[-1]}

    if data["name"] not in contacts:
        raise ValueError(f"Can't find {data['name']} name")
    else:
        contacts.update(data)

    return f"Added {data['name']} with phone {data['phone']}"


@input_error
def show_phone(tokens: list, contacts: dict) -> str:
    """
    Show the phone number associated with a given name in the given contacts dictionary.
    Args:
        tokens (list): A list of strings representing the name of the contact.
        contacts (dict): A dictionary containing the contacts.
    Returns:
        str: A string indicating the phone number associated with the given name.
    Raises:
        ValueError: If the number of tokens is less than 1, indicating that the name of the 
        contact was not provided.
    """
    if len(tokens) < 1:
        raise ValueError("Not enough arguments. Input: phone <name>")

    name = ' '.join(tokens)
    if name in contacts:
        return f"Name: {name}, phone: {contacts[name]}"

    return f"Can't find {name} name"


@input_error
def show_all(contacts: dict) -> str:
    """
    Returns a string representation of all the contacts in the dictionary.
    Parameters:
        contacts (dict): A dictionary containing the contacts.
    Returns:
        str: A string representation of all the contacts in the dictionary.
            If the dictionary is empty, returns "No contacts".
    """
    if contacts:
        return "\n".join(f"{name} : {phone}" for name, phone in contacts.items())
    else:
        return "No contacts"


def parse_input(input_str: str) -> tuple:
    command, *args = input_str.split()
    command = command.strip().lower()
    return command, *args


def main():
    contacts = dict()
    print("Welcome to the assistant bot!")
    while True:
        input_str = input("Enter command: ")
        command, *tokens = parse_input(input_str)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(tokens, contacts))
        elif command == "change":
            print(change_contact(tokens, contacts))
        elif command == "phone":
            print(show_phone(tokens, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["exit", "quit"]:
            break
        else:
            print("Invalid command.")


    print("Good bye!")


if __name__ == "__main__":
    main()
