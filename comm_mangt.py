import random
import string
import re

# Area abbreviations dictionary
area_abbreviations = {
    "Kubease": "KBS",
    "Dadease": "DSE",
    "Asenemaso": "AMO",
    "Zongo": "ZGO",
    "Boaso": "BSO",
    "Bonsu": "BSO"
}

# Member class
class Member:
    def __init__(self, id, name, email, phone_number, address, area):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.area = area

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Address: {self.address}\n"
            f"Area: {self.area}"
        )

# Generate unique member ID
def gen_id(area_abbreviation, existing_ids):
    while True:
        random_id = ''.join(random.choices(string.digits, k=4))
        member_id = f"SC-{random_id}-{area_abbreviation}"
        if member_id not in existing_ids:
            return member_id

# Get area and abbreviation
def get_area():
    while True:
        area = input("Enter area of residence (e.g Boaso): ")
        area_abbreviation = area_abbreviations.get(area)
        if area_abbreviation:
            return area, area_abbreviation
        else:
            print("Invalid area. Please enter a valid area.")

# Validate name and prevent duplicates
def validate_name(existing_names):
    while True:
        name = input("Enter name of member: ")
        if name.replace(" ", "").isalpha():
            if name not in existing_names:
                return name
            else:
                print("Name already exists.")
        else:
            print("Invalid name.")

# Validate email and prevent duplicates
def validate_email(existing_emails):
    while True:
        email = input("Enter member's email: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            if email not in existing_emails:
                return email
            else:
                print("Email already exists.")
        else:
            print("Invalid email.")

# Validate phone number
def validate_phone_number(existing_phone_numbers):
    while True:
        phone_number = input("Enter member's phone number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            if phone_number not in existing_phone_numbers:
                return phone_number
            else:
                print("Phone number already exists.")
        else:
            print("Invalid phone number.")

# Add member
def add_member(members, member_ids):
    existing_names = [member.name for member in members]
    existing_emails = [member.email for member in members]
    existing_phone_numbers = [member.phone_number for member in members]

    name = validate_name(existing_names)
    email = validate_email (input("Enter member's email"))
    phone_number = validate_phone_number(existing_phone_numbers)

    address = input("Enter address: ")
    area, area_abbreviation = get_area()

    member_id = gen_id(area_abbreviation, member_ids)
    member_ids.add(member_id)

    member = Member(member_id, name, email, phone_number, address, area)
    members.append(member)

    print("Member added successfully.")
    print(f"Unique ID: {member_id}")

# View all members
def view_members(members):
    if not members:
        print("No members to display.")
    else:
        for member in members:
            print(member)
            print("----------------------")

# Search member by ID or name
def search_member(members):
    search = input("Enter member ID or name to search: ")
    found = False

    for member in members:
        if member.id == search or member.name.lower() == search.lower():
            print(member)
            found = True
            break

    if not found:
        print("Member not found.")

# Randomly select a member
def random_member(members):
    if members:
        member = random.choice(members)
        print("Randomly selected member:")
        print(member)
    else:
        print("No members available.")

def main():
    members = []
    member_ids = set()

    while True:
        print("\n1. Add member")
        print("2. View members")
        print("3. Search member")
        print("4. Randomly select a member")
        print("5. Total members")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_member(members, member_ids)
        elif choice == "2":
            view_members(members)
        elif choice == "3":
            search_member(members)
        elif choice == "4":
            random_member(members)
        elif choice == "5":
            print(f"Total members: {len(members)}")
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()