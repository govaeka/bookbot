def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	#print(text)
	number_of_words = count_words(text)
	print(number_of_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
	list_of_words = text.split()
	return len(list_of_words)


#77986 



main()



