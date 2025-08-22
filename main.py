import sys

from stats import (
    word_count,
    character_count,
    list_sort
)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print_failure()
        sys.exit(1)
    else: 
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        words_counted = word_count(book_text)
        character_counted = character_count(book_text)
        sorted_list = list_sort(character_counted)
        print_report(file_path, words_counted, sorted_list)
    

def print_report(path, num_word, num_list):        
    print('============ BOOKBOT ============')
    print(f'Analayzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_word} total words')
    print('--------- Character Count -------')
    for i in num_list:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')
    print('============= END ===============')

def print_failure():
    print('Usage: python3 main.py <path_to_book>')

main()
