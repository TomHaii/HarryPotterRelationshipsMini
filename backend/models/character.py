class Character:
    def __init__(self, name):
        self.character_name = name
        self.aliases = []
        self.appearances_by_book = {book_num+1: [] for book_num in list(range(7))}
        self.relationship_scores_to_target_char = {}

    def populate_appearances_dict(self, books_list):
        self.appearances_by_book = {book_num+1: [] for book_num in list(range(7))}
        for book_num, book in enumerate(books_list):
            for idx, word in enumerate(book):
                if word in self.aliases:
                    self.appearances_by_book[book_num + 1].append(idx)

    def add_aliases(self, aliases):
        for alias in aliases:
            self.aliases.append(alias)
