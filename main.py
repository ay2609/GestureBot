import sys

sys.path.append('InterHand2.6M/main')
sys.path.append('InterHand2.6M/common/nets')

import torch
import torchvision
import numpy as np
import cv2
from model import get_model

DEVICE = torch.device('cpu')

param_path = 'snapshot_20.pth.tar'

model = get_model('test', 21)

params = torch.load(param_path, map_location=DEVICE)

model.load_state_dict(params['network'], strict=False)
model.eval()

transform = torchvision.transforms.ToTensor()


img = cv2.imread('hand.jpeg')
img = transform(img.astype(np.float32))/255
img = img.cpu()[None,:,:,:]



inputs = {'img': img}
targets = {}
meta_info = {}

out = model(inputs, targets, meta_info, 'test')

# -- #

hand_type = out['hand_type'][0].cpu().numpy()

right_exist = False
if hand_type[0] > 0.5:
    right_exist = True
left_exist = False
if hand_type[1] > 0.5:
    left_exist = True

print('Right hand exist: ' + str(right_exist) + ' Left hand exist: ' + str(left_exist))



