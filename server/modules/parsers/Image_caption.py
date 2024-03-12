import torch
from PIL import Image
#from lavis.models import load_model_and_preprocess

class Image_Caption:
    def __init__(self):
        self.Img = ''
        self.list = []

    def ListToString(self):
        str1 = ''
        for ele in self.list:
            str1 += ele
        return str1
    
    def Caption(self):
        # raw_image = Image.open(self.Img).convert("RGB")
        # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # model, vis_processors, _ = load_model_and_preprocess(
        #     name="blip_caption", model_type="large_coco", is_eval=True, device=device
        # )
        # vis_processors.keys()
        # image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
        # self.list = (model.generate({"image": image}))
        self.list = []