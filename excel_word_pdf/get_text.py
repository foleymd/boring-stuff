# gets a bunch of text from a word document without the styling
# example file is from http://autbor.com/demo.docx

import docx

def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

print(get_text('demo.docx'))
