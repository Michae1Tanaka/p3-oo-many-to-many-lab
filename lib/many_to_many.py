class Author:
    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(
            contract.royalties for contract in Contract.all if contract.author == self
        )


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date should be of type str.")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalties should be of type int.")
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author should be of type Author.")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book should be of type Book.")
        self.__class__.all.append(self)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date should be of type str.")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalties should be of type int.")
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author should be an instance of Author.")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book should be an instance of Book.")
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date=None):
        if date == None:
            return sorted(cls.all, key=lambda contract: contract.date)
        else:
            x = [contract for contract in cls.all if contract.date == date]
            return x.sort()


author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
contract1 = Contract(author, book1, "02/01/2001", 10)
contract2 = Contract(author, book2, "01/01/2001", 20)
contract3 = Contract(author, book3, "03/01/2001", 30)
x = Contract.contracts_by_date()
print(x == [contract2, contract1, contract3])
