
library = {
    "1984"          
    "The Hobbit"     
    "The Great Gatsby": [1, 0] }


def check_and_borrow(book_title):
    if book_title in library:
        total, borrowed = library[book_title]
        available = total - borrowed
        
        if available > 0:
            
            library[book_title][1] += 1
            return f"✅ '{book_title}' is available! You have borrowed it. ({available - 1} left)"
        else:
            return f"❌ '{book_title}' is out of stock. All copies are borrowed."
    else:
        return "❓ We do not own that book."




