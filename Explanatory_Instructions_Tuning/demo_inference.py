from inference_solver import FlexARInferenceSolver
from PIL import Image
import os
import torch
import random
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

inference_solver = FlexARInferenceSolver(
    model_path = "UVT_7B_448", #path to your model
    precision="fp16", #bf16
    target_size=448, #fixed 448
)

max_out = 1
for i in range(max_out):
    set_seed(i)
    
    ### Fixed format: Instruction + input image --> output image
    qas = [["Acknowledge the spatial structure and identify variations in light intensity, translating these into a gradient scale representing distances. Accentuate regions where light diminishes gradually, enhancing the perception of depth by dimming peripheral areas. Adjust the distribution of luminance to highlight the central vanishing point, converting detailed textures into smooth transitions of grayscale." + " <|image|>", None]]
    images = [Image.open("./demo_input_imgs/rgb_00015.jpg")]

    # qas = [["Translate the visible structures into a range of bright colors reflecting orientation angles, enhancing variations across surfaces." + " <|image|>", None]]
    # images = [Image.open("./demo_input_imgs/rgb_00015.jpg")]
    
    # qas = [["Capture the outline and prominent edges of the cylindrical object and its surroundings, simplify everything by removing textures and detailed surfaces, and emphasize only the contours and distinct features while rendering a higher contrast between light and dark regions with sharp shifts in tones." + " <|image|>", None]]
    # images = [Image.open("./demo_input_imgs/hed_input_6.jpg")]

    generated = inference_solver.generate(
        images=images,
        qas=qas,
        max_gen_len=4096,
        temperature=1.0,
        logits_processor=inference_solver.create_logits_processor(cfg=1., image_top_k=2048),
    )
    new_image = generated[1][0]
    new_image.save(f'./demo_output_{i}.png', format='PNG')