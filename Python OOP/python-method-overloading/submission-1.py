class TextProcessor:
    # Implement method overloading for format_text method
    pass

    """def format_text(self, text1: str, text2:str = None):
        if text2: 
            return text1 + text2
        else:
            return text1.upper()"""

    def format_text(self, *args:str):
        if len(args) < 2:
            return args[0].upper()
        else:
            return args[0] + args[1]


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
