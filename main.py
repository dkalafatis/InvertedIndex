import os
import string


def process_file(file_path):
    """Process a file: read its content, remove punctuation, lowercase, and tokenize."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.translate(str.maketrans('', '', string.punctuation)).lower()
        words = content.split()
    return words


def create_inverted_index(directory_path):
    """Create and return an inverted index from files in the given directory."""
    inverted_index = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            words = process_file(file_path)
            for word in words:
                if word in inverted_index:
                    inverted_index[word].add(filename)
                else:
                    inverted_index[word] = {filename}
    return inverted_index


def search_inverted_index(inverted_index):
    """Search for words in the inverted index and print the list of documents containing them."""
    while True:
        query = input("Enter search query (or type 'exit' to quit): ").lower()
        if query == 'exit':
            break
        if query in inverted_index:
            print(f"Documents containing '{query}': {', '.join(inverted_index[query])}")
        else:
            print(f"No documents contain the word '{query}'.")


def main():
    directory_path = input("Enter the path to the directory containing text files: ")
    inverted_index = create_inverted_index(directory_path)
    print("Inverted index created. You can now search for words in the documents.")
    search_inverted_index(inverted_index)


if __name__ == "__main__":
    main()
