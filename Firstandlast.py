def first_and_last(message):
    if message == (""):
        return False
    if message[0] == message[-1]:
        return True
    else: return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))