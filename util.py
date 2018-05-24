from __future__ import print_function

import torch
from torchvision.transforms import RandomCrop, ToTensor

class RandomCrops(object):
    def __init__(self, size, n_crops):
        self.size = size
        self.n_crops = n_crops
        self.rc = RandomCrop(size, padding=2)
        self.tt = ToTensor()
    
    def __call__(self, img):
        return torch.stack([self.tt(self.rc(img)) for _ in range(self.n_crops)])


class Partition(object):
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

    def __call__(self, img):
        C, W, H = img.shape
        parts = []
        part_W, part_H = W // self.n_cols, H // self.n_rows
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                parts.append(img[:, c*part_W:(c+1)*part_W, r*part_H:(r+1)*part_H])

        return torch.stack(parts)