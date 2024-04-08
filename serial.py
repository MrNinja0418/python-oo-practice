"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

class SerialGenerator:
    """Generate serial numbers."""

    def __init__(self, start):
        """Initialize with a start number."""
        self.start = start
        self.next_num = start

    def generate(self):
        """Return the next sequential number."""
        result = self.next_num
        self.next_num += 1
        return result

    def reset(self):
        """Reset the number back to the original start number."""
        self.next_num = self.start


# Testing the class
if __name__ == "__main__":
    serial = SerialGenerator(start=100)

    print(serial.generate())  # Output: 100
    print(serial.generate())  # Output: 101
    print(serial.generate())  # Output: 102

    serial.reset()
    print(serial.generate())  # Output: 100

