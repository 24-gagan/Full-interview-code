borrowed_books = {
    "member_1": ["Book A", "Book B"],
    "member_2": ["Book C"],
}

# Adding a new book to a member's record 
borrowed_books["member_1"].append("Book D")
print("Borrowed Books:", borrowed_books)