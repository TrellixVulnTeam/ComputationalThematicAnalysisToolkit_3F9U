import xmlschema
import xml.etree.ElementTree as ET
import Common.Objects.Codes as Codes
import platform

def QDACodeExporter(codes, pathname):
    codebook_element = ET.Element('CodeBook')
    codebook_element.set('origin', 'ComputationalThematicAnalysisToolkit')
    codebook_element.set('xmlns', "urn:QDA-XML:codebook:1.0")
    codebook_element.set('xmlns:xsd', "urn:QDA-XML:codebook:1.0")
    codebook_element.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    codebook_element.set('xsi:schemaLocation', "urn:QDA-XML:codebook:1.0 http://schema.qdasoftware.org/versions/Codebook/v1.0/Codebook.xsd")
    codes_element = ET.SubElement(codebook_element, 'Codes')

    def CodeToCodeElement(parent_element, code):
        new_code_element = ET.SubElement(parent_element, 'Code')
        new_code_element.set('guid', code.key)
        new_code_element.set('name', code.name)
        new_code_element.set('isCodable', 'true')
        new_code_element.set('color', '#%02x%02x%02x' % code.colour_rgb)
        desc = ET.SubElement(new_code_element, 'Description')
        if isinstance(code.notes, bytes):
            desc.text = code.notes_string
        else:
            desc.text = code.notes
        for subcode_key in code.subcodes:
            CodeToCodeElement(new_code_element, code.subcodes[subcode_key])

    for code_key in codes:
        if codes[code_key].parent == None:
            CodeToCodeElement(codes_element, codes[code_key])

    tree = ET.ElementTree(codebook_element)

    tree.write(pathname)
    #TODO figure out why function is failing with no exception on OSX after pyinstaller
    if platform.system() == 'Windows':
        codebook_schema = xmlschema.XMLSchema('./External/REFI-QDA/Codebook-mrt2019.xsd')
        codebook_schema.validate(pathname)

def QDACodeImporter(pathname):
    codes = {}
    #TODO figure out why function is failing with no exception on OSX after pyinstaller
    if platform.system() == 'Windows':
        codebook_schema = xmlschema.XMLSchema('./External/REFI-QDA/Codebook-mrt2019.xsd')
        codebook_schema.validate(pathname)

    tree = ET.parse(pathname)
    codebook_element = tree.getroot()

    def CodeElementToCode(code_element):
        code = Codes.Code(code_element.attrib['name'], code_element.attrib['guid'])
        color_hex = code_element.attrib['color'].lstrip('#')
        code.colour_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        notes = ""
        for child in list(code_element):
            if child.tag == '{urn:QDA-XML:codebook:1.0}Description':
                if child.text != None:
                    notes = notes + child.text
            if child.tag == '{urn:QDA-XML:codebook:1.0}Code':
                subcode = CodeElementToCode(child)
                subcode.parent = code
                code.subcodes[subcode.key] = subcode
        code.notes = notes
        code.notes_string = notes
        return code

    for child in list(codebook_element):
        if child.tag == '{urn:QDA-XML:codebook:1.0}Codes':
            codes_element = child
            for code_element in list(codes_element):
                code = CodeElementToCode(code_element)
                codes[code.key] = code
    return codes