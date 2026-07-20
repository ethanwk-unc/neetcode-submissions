def remove_fourth_character(word: str) -> str:
    beforeFour = word[:3]
    afterFour = word[4:]
    return beforeFour + afterFour


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
