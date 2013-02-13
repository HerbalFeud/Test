import re

pyg = 'ay'
text_in = raw_input('Enter text: ')
word_array = text_in.split(' ')
counter = 0
words = ''
punctuation = ['?', ',', '.', '!', ';']
for original in word_array:
	if re.match("^[A-Za-z0-9\.!?,;]+$", original):
		word = original.lower()
		caps_test = original[0]
		first = word[0]

		word_without_last_char = word[:-1]
		word_last_char = word[-1:]
		has_punct_error = False
		has_punct_last_character = False
		for punct in punctuation:
			if has_punct_error == False:
				has_punct_error = word_without_last_char.find(punct) != -1
			if has_punct_last_character == False:
				has_punct_last_character = word_last_char == punct

		if has_punct_error == False:

			if has_punct_last_character == True:
				word = word_without_last_char
				append_punct = word_last_char

			if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
				first_type = 'v'
			else:
				first_type = 'c'
		
			if first_type == 'v':
				new_word = word + pyg
			elif first_type == 'c':
				first_letter_slice = word[0:1]
				word_without_first_letter = word[1:]
				new_word = word_without_first_letter + first_letter_slice + pyg

			if caps_test.isupper():
				first_letter_of_new_word = new_word[0]
				first_letter_of_new_word = first_letter_of_new_word.upper()
				new_word = new_word[1:]
				new_word = first_letter_of_new_word + new_word

			if not has_punct_last_character:
				if new_word == 'aay' or new_word == 'Aay':
					new_word = 'a'

				words = words + new_word + ' '
			else:
				if new_word == 'aay' or new_word == 'Aay':
					new_word = 'a'
				words = words + new_word + append_punct + ' '

		else:
			print "error"
	else:
		print "error"

print words