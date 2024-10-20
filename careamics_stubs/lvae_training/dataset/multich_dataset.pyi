import numpy as np
from .config import DatasetConfig as DatasetConfig
from .types import DataSplitType as DataSplitType, TilingMode as TilingMode
from .utils.empty_patch_fetcher import EmptyPatchFetcher as EmptyPatchFetcher
from .utils.index_manager import GridIndexManager as GridIndexManager
from .utils.index_switcher import IndexSwitcher as IndexSwitcher
from _typeshed import Incomplete
from typing import Callable

class MultiChDloader:
    Z: int
    def __init__(self, data_config: DatasetConfig, fpath: str, load_data_fn: Callable, val_fraction: float = None, test_fraction: float = None) -> None: ...
    def disable_noise(self) -> None: ...
    def enable_noise(self) -> None: ...
    def get_data_shape(self): ...
    def load_data(self, data_config, datasplit_type, load_data_fn: Callable, val_fraction: Incomplete | None = None, test_fraction: Incomplete | None = None, allow_generation: Incomplete | None = None): ...
    def save_background(self, channel_idx, frame_idx, background_value) -> None: ...
    def get_background(self, channel_idx, frame_idx): ...
    def remove_background(self) -> None: ...
    def rm_bkground_set_max_val_and_upperclip_data(self, max_val, datasplit_type) -> None: ...
    def upperclip_data(self) -> None: ...
    def compute_max_val(self): ...
    max_val: Incomplete
    def set_max_val(self, max_val, datasplit_type) -> None: ...
    def get_max_val(self): ...
    def get_img_sz(self): ...
    def get_num_frames(self): ...
    def reduce_data(self, t_list: Incomplete | None = None, h_start: Incomplete | None = None, h_end: Incomplete | None = None, w_start: Incomplete | None = None, w_end: Incomplete | None = None) -> None: ...
    def get_idx_manager_shapes(self, patch_size: int, grid_size: int | tuple[int, int, int]): ...
    idx_manager: Incomplete
    def set_img_sz(self, image_size, grid_size: int | tuple[int, int, int]): ...
    def __len__(self) -> int: ...
    def set_repeat_factor(self) -> None: ...
    def get_begin_end_padding(self, start_pos, end_pos, max_len): ...
    def get_mean_std(self): ...
    def set_mean_std(self, mean_val, std_val) -> None: ...
    def normalize_img(self, *img_tuples): ...
    def normalize_input(self, x): ...
    def normalize_target(self, target): ...
    def get_grid_size(self): ...
    def get_idx_manager(self): ...
    def per_side_overlap_pixelcount(self): ...
    def compute_individual_mean_std(self): ...
    def compute_mean_std(self, allow_for_validation_data: bool = False): ...
    def replace_with_empty_patch(self, img_tuples): ...
    def get_mean_std_for_input(self): ...
    def get_uncorrelated_img_tuples(self, index): ...
    def __getitem__(self, index: int | tuple[int, int]) -> tuple[np.ndarray, np.ndarray]: ...
