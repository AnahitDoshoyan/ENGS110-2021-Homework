import json

def displayAllBooks(books):
	print("")
	for current_book in books:
		for current_key in current_book:
			print(current_key, ":", current_book[current_key])

def getNumericInput(displayString):
	while(True):
		user_data = input(displayString)
		if(user_data.isnumeric()):
			user_data = int(user_data)
			return user_data
		else:
			print("Please insert a number")

def addBook():
	book = {
		"title" : "", 
		"num_of_pages" : 0,  
		"language" : "", 
		"author" : "", 
		"publishing_year" : 0,
		"last_time_read" : {
            		"day" : 0,
           		"month" : "",
            		"year" : 0
        	},
        	"chapters" : []
	}

	book["title"] = input("Please insert the title: ")
	book["num_of_pages"] = getNumericInput("Please insert the number of pages: ")
	book["language"] = input("Please insert the language: ")
	book["author"] = input("Who is the author: ")
	book["publishing_year"] = getNumericInput("PLease insert the year of publishing: ")
	last_time_read = input("When did you last read this?: Please insert date with the following format: DD/MM/YYYY ")
	last_time_read = last_time_read.split("/")
	book["last_time_read"]["day"] = int( last_time_read[0])
	book["last_time_read"]["month"] = last_time_read[1]
	book["last_time_read"]["year"] = int(last_time_read[2])
	while(True):
		chapter = input("Please insert a chapter to the book and insert END to finish adding chapters")
		if (chapter == "END"):
			break
		else:
			book["chapters"].append(chapter)

	return book

def loadExistingBooks():
	with open('books.json') as file_data:
		print(file_data)
		books = json.load(file_data)
		return books

def saveToTheFile(books):
	f = open("books.json", "w")
	print(books)
	f.write(json.dumps(books, indent=2))
	f.close()

def main():
	books = []

	books = loadExistingBooks()

	while(True):
		insert_mode = input("Do you want to start adding books?, please answer yes or no")
		if(insert_mode == "no"):
			print("Goodbye")
			break
		else:
			book = addBook()
			books.append(book)

	print("Saving to the file")
	saveToTheFile(books)
	displayAllBooks(books)

    break
 47                 else:
 48                         book["chapters"].append(chapter)
 49 
 50         return book
 51 
 52 def loadExistingBooks():
 53         with open('books.json') as file_data:
 54                 print(file_data)
 55                 books = json.load(file_data)
 56                 return books
 57 
 58 def saveToTheFile(books):
 59         f = open("books.json", "w")
 60         print(books)
 61         f.write(json.dumps(books, indent=2))
 62         f.close()
 63 
 64 def main():
 65         books = []
 66 
 67         books = loadExistingBooks()
 68 
 69         while(True):
 70                 insert_mode = input("Do you want to start adding books?, please answer yes or no")
 71                 if(insert_mode == "no"):
 72                         print("Goodbye")
 73                         break
 74                 else:
 75                         book = addBook()
 76                         books.append(book)
 77 
 78         print("Saving to the file")
 79         saveToTheFile(books)
 80         displayAllBooks(books)
 81 
 82 main()                                                                                                                                                                        
                                      main()
