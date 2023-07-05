# Python - Inheritance

This project demonstrates the concept of inheritance in Python. Inheritance is a fundamental feature of object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes.

## Overview

In this project, we have implemented a base class called `Base` and a derived class called `User`. The `Base` class serves as the parent class, while the `User` class is the child class that inherits from `Base`.

## Class Structure

### Base

The `Base` class represents a base class with a single attribute `id` and a class variable `__nb_instances` to keep track of the number of instances created.

#### Methods

- `__init__(self)`: Initializes the `Base` object, increments the `__nb_instances` class variable, and assigns a unique `id` to the instance.

### User

The `User` class is a derived class that inherits from the `Base` class. It does not define any additional attributes or methods.

## Usage

To use the classes defined in this project, follow these steps:

1. Instantiate a `User` object: `u = User()`
2. Access the `id` attribute of the `User` object: `print(u.id)`

## Examples

Here are some examples of using the classes:

```python
# Example 1: Creating a single User instance
u = User()
print(u.id)  # Output: <id_value>

# Example 2: Creating multiple User instances
for i in range(3):
    u = User()
print(u.id)  # Output: <id_value>

# Example 3: Accessing the User class through the Base class
b = Base()
u = User()
print(u.id)  # Output: <id_value>
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open a new issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
