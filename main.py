# Functional Solution
def flatten_and_sort(arr):
    # Flatten the list of integers and sort it in ascending order
    flattened = sorted([num for sublist in arr for num in sublist])
    return flattened

# Ensure data immutability: In this solution, we create a new list 'flattened' with the sorted values, leaving the original 'arr' unchanged.
# This solution is a pure function because it produces the same output for the same input and has no side effects.
# It is not a higher-order function because it does not take or return functions.
# Functional programming is helpful in this case because it enforces a clear separation of concerns and allows us to work with immutable data, which can lead to more predictable and testable code.

# Object-Oriented Solution
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"

# This solution demonstrates the four pillars of OOP:
# - Encapsulation: Data (max_speed, condition, price) and behavior (repair, boost, flame_jet) are encapsulated within classes.
# - Abstraction: The classes abstract away the implementation details from the client code.
# - Inheritance: Subclasses (AnakinsPod and SebulbasPod) inherit attributes and methods from the base class (Podracer).
# - Polymorphism: While not explicitly demonstrated, polymorphism can be achieved by method overriding, allowing different behaviors based on the actual object's class.

# Functional vs. OOP:
# Both paradigms have their strengths. Functional programming is suitable for data transformation tasks and situations where immutability is important. OOP is beneficial for modeling real-world entities with state and behavior. Choosing between them depends on the problem at hand.

# Personal Preferences:
# Preferences may vary from one programmer to another. Some may prefer functional programming for its simplicity and predictability, while others may find OOP more intuitive for certain tasks.

# Use Cases:
# Functional programming is well-suited for data processing, transformations, and pure functions. OOP is ideal for modeling complex systems, with well-defined entities and their interactions.

# Understanding:
# Understanding each paradigm depends on prior programming experience and the context in which it's applied. To deepen understanding, one should practice and work on real-world projects using both paradigms.


