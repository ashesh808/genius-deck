from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from lavis.models import load_model_and_preprocess
import torch
from PIL import Image as Im
import io


def ListToString(list):
    str1 = ''

    for ele in list:
        str1 += ele

    return str1

def Caption(path):

    raw_image = Im.open(path).convert("RGB")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # we associate a model with its preprocessors to make it easier for inference.
    model, vis_processors, _ = load_model_and_preprocess(
        name="blip_caption", model_type="large_coco", is_eval=True, device=device
    )
    # uncomment to use base model
    # model, vis_processors, _ = load_model_and_preprocess(
    #     name="blip_caption", model_type="base_coco", is_eval=True, device=device
    # )
    vis_processors.keys()

    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    return(model.generate({"image": image}))

def PptToText(PPTX_Path, Flag=bool):
    prs = Presentation(PPTX_Path)
    f = open('powerpoint.txt','a') #change to final location
    for slide_number, slide in enumerate(prs.slides):
        #print(f"Slide {slide_number + 1}:")
        x = str(slide_number)
        f.write("Slide " + x + "\n")
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                f.write(shape.text)
                #print(shape.text)
            elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE and Flag != True:
                txt = 'An image depicting '
                Image = shape.image
                Image_bytes = Image.blob
                Image = io.BytesIO(Image_bytes)
                text = ListToString(Caption(Image))
                text.strip('['']')
                text = txt + text + '/n'
                f.write(text)
                

    f.close()

if __name__ == '__main__':
    pptx = input()
    PptToText(pptx, False)