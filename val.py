import lxml.etree
xml_file = lxml.etree.parse("sample.xml")
xml_validator = lxml.etree.XMLSchema(file="schema.xsd")

is_valid = xml_validator.validate(xml_file)

print(is_valid)
