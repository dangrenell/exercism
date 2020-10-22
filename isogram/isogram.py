def is_isogram(string):
    for char in " -":
        string = string.replace(char, "")
    string = string.lower()
    return len(string) == len(set(string))
