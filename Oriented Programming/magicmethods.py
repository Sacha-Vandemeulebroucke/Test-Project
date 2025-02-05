# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allows developers to define or customize the behavior of objects
#
# to see more magic methods : https://www.geeksforgeeks.org/dunder-magic-methods-python/

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __le__(self, other):
        return self.num_pages <= other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        match key:
            case 'title':
                return self.title
            case 'author':
                return self.author
            case 'pages':
                return self.num_pages
            case _:
                return f"Key {key} was not found"



book1 = Book("The hobbit", "Tolkien", 310)
book2 = Book("Harry Potter", "J.K Rowling", 500)
book3 = Book("Les misérables", "Victor Hugo", 990)
book4 = Book("Les misérables", "Victor Hugo", 990)

books = [book1, book2, book3]

for book in books:
   print(book['lol'])


# print(book <= book2)
# print(book < book2)

# print(book3 == book4)
print(book3 + book2)

print("misérables" in book2)
print(book1['pages'])