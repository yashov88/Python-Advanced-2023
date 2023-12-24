import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4

VALID_DOMAINS = (".com", ".bg", ".net", ".org")

patten_name = r"\w+"
patten_domain = r"\.[a-z]+"

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")

    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if re.findall(patten_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name can contain only letters, digits and underscores!")

    if re.findall(patten_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
