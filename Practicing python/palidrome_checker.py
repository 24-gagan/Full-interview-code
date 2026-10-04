def palidrome():
    text = input("Enter the word or phrase")
    cleaned_text = text.replace(" ", "").lower()
    if cleaned_text == cleaned_text[::-1]:
        print("It is a palidrome")
    else:
        print("It is not a palidrome")


if __name__ == "__main__":
    palidrome()
