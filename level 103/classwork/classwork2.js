class Book {
  constructor(title, author) {
    this.title = title;   
    this.author = author; 
  }

  describe() {
    console.log("The book " + this.title + " is written by " + this.author + ".");
  }
}

const myBook = new Book("Harry Potter", "J.K. Rowling");
myBook.describe(); 
