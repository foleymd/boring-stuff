''' reading and editing word documents

https://python-docx.readthedocs.io/en/latest/ - lots of extras here

demo files are from:
https://automatetheboringstuff.com/src/meetingminutes1.pdf
https://automatetheboringstuff.com/src/meetingminutes2.pdf
https://automatetheboringstuff.com/demo.docx
'''

import os, docx # latter is python-docx

# document object contains paragraph objects

d = docx.Document('demo.docx')

print(d.paragraphs) # all paragraph objects

print(d.paragraphs[0]) # first paragraph objectt

print(d.paragraphs[0].text) # text member variable contains text

print(d.paragraphs[1].text)

p = d.paragraphs[1] # don't use text member variable because you want to loop over it next

#paragraphs contain run objects; a new run starts every time the style on a paragraph changes

for run in p.runs:
    if run.bold == True:
        print('\'' + run.text + '\' is bold')
    if run.italic == True:
        print('\'' + run.text + '\' is italic')    
    print(run.text)

# underlines and modifies text content
p.runs[3].underline = True
p.runs[3].text = 'italic and underlined.'

# saves document on hard drive
d.save('demo2.docx')

# styles of text match Word styles, e.g. Normal, Header 1, etc.

p.style = 'Title'
d.save('demo3.docx')

# creates new document in memory
d = docx.Document()

#adds first and second paragaphs
d.add_paragraph('Hi I am a new paragraph.')

d.add_paragraph('I am the second paragraph.')
d.save('demo4.docx')

# open first paragraph and add a new run, making it bold and saving the doc
p = d.paragraphs[0]
p.add_run('This is a new run')
p.runs[1].bold = True

d.save('demo5.docx')

'''no way to insert paragraphs or runs, you need to append
  if you want to modify, you'll need to create a new document and
  creating paragraph and run changes as you go'''

