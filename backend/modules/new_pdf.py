import fitz
import io
from PIL import Image as Im
import torch
from lavis.models import load_model_and_preprocess


def ListToString(list):
    str1 = ''

    for ele in list:
        str1 += ele

    return str1

def Caption(path):
    raw_image = Im.open(path).convert('RGB')

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

def ReadPdf(File_Path=str, Flag=bool):
    txt = "An image depicting "
    doc = fitz.open(File_Path)
    out = open('output.txt', 'wb')
    for page_index in range(len(doc)):
        page = doc[page_index]
        text = page.get_text().encode("utf-8")
        pgnum = bytes((f"Page {page_index + 1}\n"), "utf-8")
        out.write(pgnum)
        out.write(text)
        out.write(bytes((12,)))

        if Flag != True:
            image_list = page.get_images()

            for image_index, img in enumerate(image_list, start=1):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                text = ListToString(Caption(io.BytesIO(pix.tobytes()))) # First I take the pixel map and turn it into bytes. Then I use the IO.BytesIO to turn it into a string of bytes. Then I pass that into the image captioning function which returns a list and finally i turn the lsit into a string.
                text.strip('['']')
                text = txt + text + '\n'
                out.write(bytes(text, "UTF-8"))
                pix = None

    out.close()

if __name__ == '__main__':
    pdf = input('Path')
    ReadPdf(pdf, False)
