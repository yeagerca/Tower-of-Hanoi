class Tower:
    """A stack representing a tower. Each element must be smaller than the element before it."""

    def __init__(self):
        self.stack = []

    def build_tower(self, size):
        """Clear the stack then fill append integers descending from "size" to 1.

        Keyword arguments:
        size -- desired number of elements in the stack.
        """
        self.stack = []
        while size > 0:
            self.stack.append(size)
            size -= 1

    def top(self):
        """Return the top element of the tower."""
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def push(self, number):
        """Append a number element to the top of the tower. Return 0 if failed. Return 1 if succeeded.

        Keyword arguments:
        number -- the value to append.
        """
        if number >= self.top():
            return 0
        else:
            self.stack.append(number)
            return 1

    def pop(self):
        """Remove the top element from the tower."""
        self.stack.pop()

    def to_string(self):
        """Return the stack as a string."""
        return str(self.stack)


if __name__ == '__main__':

    my_tower = Tower()
    my_tower.build_tower(2)
    print("tower:\t\t\t", my_tower)
    print("str(tower):\t\t", str(my_tower))
    print(".to_string():\t", my_tower.to_string())
    print(".stack:\t\t\t", my_tower.stack)
    print(".top():\t\t\t", my_tower.top())

    my_tower.build_tower(2)
    print(my_tower.stack)