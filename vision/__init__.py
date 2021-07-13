from .datasets import CelebADataset
from .datasets import QuickDrawFaceDataset

Datasets = {
    "celeba": CelebADataset,
    "face": QuickDrawFaceDataset
}
