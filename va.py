import lxml.etree
xml_file = lxml.etree.parse("sa.xml")
xml_validator = lxml.etree.XMLSchema(file="sc.xsd")

is_valid = xml_validator.validate(xml_file)

print(is_valid)
