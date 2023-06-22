import torch
from torch.utils.data import Dataset
import numpy as np

class Dataset(Dataset):
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    def __len__(self):
        if "train" in self.in_dir:
            return 612
        elif "test" in self.in_dir:
            return 36
        else:
            return 0

    def __getitem__(self, idx):
        input_data = torch.tensor(np.load(self.in_dir))
        output_data = torch.tensor(np.load(self.out_dir))
        return input_data, output_data