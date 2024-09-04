class Book: 
    def __init__(self, author, title, year, available_copies, edition):
        self.author = author
        self.title = title
        self.year = year
        self.available_copies = available_copies
        self.edition = edition

    def display_info(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.author}")
        print(f"Year: {self.year}")
        print(f"Available copies: {self.available_copies}")
        print(f"Edition: {self.edition}")

    def is_available(self):
        return self.available_copies > 0
    
    def update_available_copies(self, num_copies):
        if num_copies >= 0:
            self.available_copies = num_copies
        else:
            print("Invalide number of copies, copies shouldn't be negative numbers")

class member:
    def __init__(self, name, member_id, book_brrowed):
        self.member_id = member_id
        self.name = name 
        self.book_brrowed = book_brrowed

    def display_infor(self):
        print()





        