
class BookStore:
    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Name of the book is : "+self.Name)
        print("Author of the book is : ",self.Author)
        print("Number of books are : ",BookStore.NoOfBooks)
    
def main():

    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()
    obj2 = BookStore("C programming ","Dennis Ritche")
    obj2.Display()

if __name__ == "__main__":
    main()