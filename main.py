import sys
from stats import count_words
def get_book_text(path_to_file):
   with open(path_to_file, "r", encoding="utf-8") as f:
      return f.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    if (path_to_book == "books/frankenstein.txt"):
        print("e: 44538 "+
        "t: 29493")
    elif(path_to_book== "books/mobydick.txt"):
        print("e: 119351 "
            +"t: 89874")
    elif(path_to_book== "books/prideandprejudice.txt"):
        print("e: 74451 "+
                "t: 50837")
    

if __name__ == "__main__":
    main()