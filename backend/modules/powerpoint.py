import os
from pptx import Presentation

pptx = input()

prs = Presentation(pptx)
f = open('powerpoint.txt','a')
for slide_number, slide in enumerate(prs.slides):
    #print(f"Slide {slide_number + 1}:")
    x = str(slide_number)
    f.write("Slide " + x + "\n")
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            f.write(shape.text)
            #print(shape.text)
f.close()