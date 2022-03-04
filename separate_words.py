

# függvény paraméterül kap szavakat
# és összefűzi őket, elválasztja őket vesszővells ezzel tér vissza
# DE az uccsó elem után ne legyen vessző

def concat_words(words):
    result = ""
    counter = 1
    for word in words:
        result += word
        if counter != len(words):
            result += ","
        counter += 1
    return result


print(concat_words(["a","b", "asdfa", "asdfdfff", "asdfv"]))