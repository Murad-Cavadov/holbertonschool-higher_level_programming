#!/usr/bin/env python3
"""
Bu modul Python lüğətlərini XML formatına seriyallaşdırmaq və
yenidən lüğətə qaytarmaq üçün funksiyaları ehtiva edir.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Lüğəti XML formatına çevirir və fayla yadda saxlayır.

    Args:
        dictionary (dict): Seriyallaşdırılacaq məlumat.
        filename (str): Çıxış faylının adı.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    XML faylını oxuyur və onu Python lüğətinə çevirir.

    Args:
        filename (str): Oxunacaq XML faylının adı.

    Returns:
        dict: Deseriyallaşdırılmış məlumat lüğəti.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError):
        return None
