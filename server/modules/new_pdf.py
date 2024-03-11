import fitz
import io
from modules.Image_caption import Image_Caption
import os

class PdfParse(Image_Caption):
    def __init__(self, pdf_path, file_name, Skip_image):
        self.pdf_path = os.path.join(pdf_path, file_name + '.pdf')
        self.Flag = Skip_image

    def ReadPdf(self):
        data = b''
        txt = "An image depicting "
        doc = fitz.open(self.pdf_path)
        #out = open('output.txt', 'wb')
        for page_index in range(len(doc)):
            page = doc[page_index]
            text = page.get_text().encode("utf-8")
            pgnum = bytes((f"Page {page_index + 1}\n"), "utf-8")
            #out.write(pgnum)
            data += pgnum
            #out.write(text)
            data += text
            #out.write(bytes((12,)))
            data += bytes((12,))

            if self.Flag != 'True':
                image_list = page.get_images()

                for image_index, img in enumerate(image_list, start=1):
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)

                    if pix.n - pix.alpha > 3:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    self.Img = io.BytesIO(pix.tobytes())
                    PdfParse.Caption(self)
                    text = PdfParse.ListToString(self) # First I take the pixel map and turn it into bytes. Then I use the IO.BytesIO to turn it into a string of bytes. Then I pass that into the image captioning function which returns a list and finally i turn the lsit into a string.
                    text.strip('['']')
                    text = txt + text + '\n'
                    #out.write(bytes(text, "UTF-8"))
                    data += bytes(text, "utf-8")
                    pix = None

        #out.close()
        Whole_text = data.decode()
        return(Whole_text)

if __name__ == '__main__':
    path = input()
    name = input()
    img = False
    test = PdfParse(path, name, img)
    test.ReadPdf()
