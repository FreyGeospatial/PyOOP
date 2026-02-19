# we already know about how __init__ initiallizes a class instance with certain attributes, like so:

class InitExample:
    def __init__(self):
        self.x = 42


blah = InitExample()
print(blah.x)


###############################################
# Other dunder methods
# __enter__
# __aenter__
# __repr__
# __str__