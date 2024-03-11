import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

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

        raw_image = Image.open(self.Img).convert("RGB")

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
        print("doing something")

        image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
        self.list = (model.generate({"image": image}))