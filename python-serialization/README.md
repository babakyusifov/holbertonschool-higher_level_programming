Python - Serialization
 Novice
 By: Javier Valenzani
 Weight: 1
 Your score will be updated as you progress.
Description
For this project, we expect you to look at these concepts:

OOP - Marshaling and Serialization
C - Marshaling and Byte Order
Python - Serialization
Introduction:
Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

What is Marshaling?
Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

What is Serialization?
Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

Learning Objectives:
Articulate the differences and similarities between marshaling and serialization.
Implement serialization in a practical programming task.
Understand how serialized data can be used in web applications, databases, and network communications.
Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.
Resources:
Real Python Serialization
Real Python: Working With JSON Data in Python
Python’s pickle documentation
Corey Schafer on Pickle
CSV to JSON in Python
Python XML ElementTree Guide
Socket Programming Guide
This project will equip you with the skills needed to manipulate and manage data effectively, preparing you for more advanced topics in computer science and software development. Get ready to build a solid foundation in data handling that will support your future projects and career in the technology sector.

Tasks
0. Basic Serialization
mandatory
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

Instructions:
Write a Python module named task_00_basic_serialization.py with the following functions:

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
The function serialize_and_save_to_file take 2 parameters:

data: A Python Dictionary with data
filename: The filename of the output JSON file. If the output file already exists it should be replaced.
The function load_and_deserialize take 1 parameters:

filename: The filename of the input JSON file This function returns a Python Dictionary with the deseialized JSON data from the file.
Execution Output Example:
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-serialization
File: task_00_basic_serialization.py
 
0/5 pts
1. Pickling Custom Classes
mandatory
Learn how to serialize and deserialize custom Python objects using the pickle module.

Instructions:
1 - Create a custom Python class named CustomObject. This class should have the following attributes:

name (a string)
age (an integer)
is_student (a boolean)
Additionally, the class should have a method display method to print out the object’s attributes with the following format:

Name: John
Age: 25
Is Student: True
2 - Implement two methods within this class:

serialize(self, filename): This method will take a filename as its parameter. Using the pickle module, it will serialize the current instance of the object and save it to the provided filename.
@classmethod deserialize(cls, filename): This class method will take a filename as its parameter. Using the pickle module, it will load and return an instance of the CustomObject from the provided filename.
3 - Save your code in a file named task_01_pickle.py.

Make sure to handle possible exceptions for non-existent or malformed files. If this happens, the methods should return None

Sample Test:
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
Output:

Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-serialization
File: task_01_pickle.py
 
0/4 pts
2. Converting CSV Data to JSON Format
mandatory
The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

Instructions:
Begin by importing the required modules: python import csv import json

Define a function named convert_csv_to_json that takes the CSV filename as its parameter and writes the JSON data to data.json.

Inside this function:

Use Python’s csv module to open the CSV file and read the data. Use the DictReader class to convert each row into a dictionary.
Serialize the list of dictionaries using the json module.
Write the serialized JSON data to data.json.
The function should return True if the conversion was successful.

Handle exceptions, such as file not found. Function should return False in this case.

Save your work in task_02_csv.py.

Testing Your Code:
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
$ python3 main_02_csv.py 
Data from data.csv has been converted to data.json
CSV Dataset (data.csv) example:
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
After the conversion, the resulting data.json file should contain:

[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-serialization
File: task_02_csv.py
 
0/2 pts
3. Serializing and Deserializing with XML
mandatory
In this exercise we’ll explore serialization and deserialization using XML as an alternative format to JSON.

Instructions:
Begin by importing the required modules. You can use the xml.etree.ElementTree module which is a part of Python’s standard library for XML processing:
   import xml.etree.ElementTree as ET
Define two main functions:
serialize_to_xml(dictionary, filename): This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.

deserialize_from_xml(filename): This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.

For serialize_to_xml:
Create a root element, e.g., <data>.
Iterate through the dictionary items and add them as child elements to the root.
Write the XML tree to the provided filename using the ET.ElementTree class.
For deserialize_from_xml:
Parse the XML file using ET.parse.
Navigate through the XML elements to reconstruct the dictionary.
Return the constructed dictionary.
Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.

Save your work in task_03_xml.py.

Testing Your Code:
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
Output:
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
data.xml

<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-serialization
File: task_03_xml.py
