from ..config import InferenceConfig as InferenceConfig
from ..config.transformations import NormalizeModel as NormalizeModel
from .dataset_utils import reshape_array as reshape_array
from _typeshed import Incomplete
from careamics.transforms import Compose as Compose
from numpy.typing import NDArray as NDArray
from torch.utils.data import Dataset

class InMemoryPredDataset(Dataset):
    pred_config: Incomplete
    input_array: Incomplete
    axes: Incomplete
    image_means: Incomplete
    image_stds: Incomplete
    data: Incomplete
    patch_transform: Incomplete
    def __init__(self, prediction_config: InferenceConfig, inputs: NDArray) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> NDArray: ...
