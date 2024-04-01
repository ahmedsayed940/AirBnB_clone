# 0x00. AirBnB Clone - The Console

## Description
This project is part of the ALX SE Programme and aims to build a simplified version of the AirBnB website. In this specific module, we focus on developing a command-line interface (CLI) known as the console, which allows users to interact with the application through a command prompt.

## Description of the Command Interpreter
The command interpreter, or console, is a Python script that serves as the primary interface for interacting with the AirBnB clone application. It provides a set of commands to perform various actions such as creating, updating, deleting, and displaying instances of different classes within the application.

### How to Start the Console, How to Use the Console, Once the console is started, you can use it to interact with the AirBnB clone application. Here are some basic commands and usage instructions:
To start the console, follow these steps:
1. Clone the AirBnB clone repository to your local machine.
2. Navigate to the directory containing the console script (`console.py`).
3. Open a terminal window.
4. Run the console script using Python:
  $ ./console.py

### How to Use the Console
Once the console is started, you can use it to interact with the AirBnB clone application. Here are some basic commands and usage instructions:

## Creating an Instance:
To create a new instance of a class, use the create command followed by the class name. For example:
'''bash
(hbnb) create BaseModel
'''

## Showing an Instance:
To display the details of a specific instance, use the show command followed by the class name and instance ID. For example:
```bash
(hbnb) show BaseModel 1234-5678
```

## Deleting an Instance:
To delete an instance, use the destroy command followed by the class name and instance ID. For example:
```bash
(hbnb) destroy BaseModel 1234-5678
```

## Displaying All Instances:
To display all instances of a specific class or all classes, use the all command followed by an optional class name. For example:
```bash
(hbnb) all BaseModel
(hbnb) all
```

## Updating an Instance:
To update the attributes of an instance, use the update command followed by the class name, instance ID, attribute name, and new attribute value. For example:
```bash
(hbnb) update BaseModel 1234-5678 name "New Name"
```

### Examples
Here are some examples of using the console to perform various actions:

## Create a new user instance:
```bash
(hbnb) create User
```

## Show details of a specific place instance:
```bash
(hbnb) show Place 1234-5678
```

## Delete an amenity instance:
```bash
(hbnb) destroy Amenity 8765-4321
```

## Display all instances of the review class:
```bash
(hbnb) all Review
```

## Update the name attribute of a state instance:
```bash
(hbnb) update State 9876-5432 name "New York"
```

## These are just a few examples of how to use the console. Refer to the help command (help) for a list of all available commands and their usage.

#### Authors

- Abdullah Hussein
- Ahmed Sayed Salih Sayed
