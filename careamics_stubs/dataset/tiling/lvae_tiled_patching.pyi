import numpy as np
from careamics.config.tile_information import TileInformation as TileInformation
from careamics.lvae_training.dataset.utils.index_manager import GridIndexManager as GridIndexManager
from numpy.typing import NDArray as NDArray
from typing import Any, Generator

def extract_tiles(arr: NDArray, tile_size: NDArray[np.int_], overlaps: NDArray[np.int_], padding_kwargs: dict[str, Any] | None = None) -> Generator[tuple[NDArray, TileInformation], None, None]: ...
def compute_tile_info_legacy(grid_index_manager: GridIndexManager, index: int) -> TileInformation: ...
def compute_tile_info(tile_grid_indices: NDArray[np.int_], data_shape: NDArray[np.int_], tile_size: NDArray[np.int_], overlaps: NDArray[np.int_], sample_id: int = 0) -> TileInformation: ...
def compute_padding(data_shape: NDArray[np.int_], tile_size: NDArray[np.int_], overlaps: NDArray[np.int_]) -> tuple[tuple[int, int], ...]: ...
def n_tiles_1d(axis_size: int, tile_size: int, overlap: int) -> int: ...
def total_n_tiles(data_shape: tuple[int, ...], tile_size: tuple[int, ...], overlaps: tuple[int, ...]) -> int: ...
def compute_tile_grid_shape(data_shape: NDArray[np.int_], tile_size: NDArray[np.int_], overlaps: NDArray[np.int_]) -> tuple[int, ...]: ...
