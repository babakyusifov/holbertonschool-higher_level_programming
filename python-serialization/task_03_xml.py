#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration=True, encoding='utf-8')


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text

    return data_dict
