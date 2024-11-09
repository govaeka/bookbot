def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	#print(text)
	number_of_words = count_words(text)
	print(number_of_words)
	letter_count = count_characters(text)
	print(letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(tw):
	list_of_words = tw.split()
	return len(list_of_words)


def count_characters(tc):
	tc = tc.lower()
	ledger = {}
	for letter in tc:
		if letter in ledger:
			ledger[letter] += 1
		else:
			ledger[letter] = 1
	return ledger


main()



