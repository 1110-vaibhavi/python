def count_repeated_chars(text):
    frequencies={}
    for char in text:
        frequencies[char]=frequencies.get(char,0)+1
    repeated={char:count for char,count in frequencies.items() if count >1}
    sorted_repeated=sorted(repeated.items(),key=lambda x:x[1],reverse=True)
    for char,count in sorted_repeated:
        print(f"{char}{count}")

string="thequickbrownfoxjumps"
count_repeated_chars(string)