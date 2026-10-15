class Publication:
    def __init__(self, title: str, author: str):
      self._title = title
      self._author = author
      
    def get_title(self) -> str:
      return self._title

    def set_title(self, title: str):
      self._title = title

    def get_author(self) -> str:
      return self._author

    def set_author(self, author: str):
      self._author = author

    def display_info(self):
      print("Publication Information:")
      print(f"Title: {self.get_title()}")
      print(f"Author: {self.get_author()}\n")

    def number_pages(self) -> int:
      return self.number_pages

    def get_number_pages(self) -> str:
      return self._number_pages

    def set_number_pages(self, title: str):
      self._number_ages = number_pages








  











class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self._number_pages = number_pages

    # Getters and Setters
    def get_number_pages(self) -> int:
        return self._number_pages

    def set_number_pages(self, number_pages: int):
        self._number_pages = number_pages

    def display_info(self):
        print("Book Information:")
        # Validation condition matching the output warning
        if self.get_number_pages() <= 0:
            print("Number of pages must be positive.")
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"Number of pages: {self.get_number_pages()}\n")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self._issue_number = issue_number

    # Getters and Setters
    def get_issue_number(self) -> int:
        return self._issue_number

    def set_issue_number(self, issue_number: int):
        self._issue_number = issue_number

    def display_info(self):
        print("Magazine Information:")
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"Issue number: {self.get_issue_number()}\n")


if __name__ == "__main__":
    # Test Case 1: Publication
    pub = Publication("The New York Times", "H. Raymond & G. Jones")
    pub.display_info()
    
    # Test Case 2: Book
    book = Book("The Duke and I", "J. Quinn", 480)
    book.display_info()
    
    # Test Case 3: Magazine
    mag = Magazine("The New Yorker", "D. Remnick", 80)
    mag.display_info()

