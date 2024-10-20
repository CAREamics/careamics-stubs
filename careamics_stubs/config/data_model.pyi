from .support import SupportedTransform as SupportedTransform
from .transformations import N2VManipulateModel as N2VManipulateModel, TRANSFORMS_UNION as TRANSFORMS_UNION
from .validators import check_axes_validity as check_axes_validity, patch_size_ge_than_8_power_of_2 as patch_size_ge_than_8_power_of_2
from _typeshed import Incomplete
from numpy.typing import NDArray as NDArray
from pydantic import BaseModel
from typing import Literal
from typing_extensions import Self

def np_float_to_scientific_str(x: float) -> str: ...

Float: Incomplete

class DataConfig(BaseModel):
    model_config: Incomplete
    data_type: Literal['array', 'tiff', 'custom']
    axes: str
    patch_size: list[int]
    batch_size: int
    image_means: list[Float] | None
    image_stds: list[Float] | None
    target_means: list[Float] | None
    target_stds: list[Float] | None
    transforms: list[TRANSFORMS_UNION]
    dataloader_params: dict | None
    @classmethod
    def all_elements_power_of_2_minimum_8(cls, patch_list: list[int]) -> list[int]: ...
    @classmethod
    def axes_valid(cls, axes: str) -> str: ...
    @classmethod
    def validate_prediction_transforms(cls, transforms: list[TRANSFORMS_UNION]) -> list[TRANSFORMS_UNION]: ...
    def std_only_with_mean(self) -> Self: ...
    def validate_dimensions(self) -> Self: ...
    def has_n2v_manipulate(self) -> bool: ...
    def add_n2v_manipulate(self) -> None: ...
    def remove_n2v_manipulate(self) -> None: ...
    def set_means_and_stds(self, image_means: NDArray | tuple | list | None, image_stds: NDArray | tuple | list | None, target_means: NDArray | tuple | list | None | None = None, target_stds: NDArray | tuple | list | None | None = None) -> None: ...
    def set_3D(self, axes: str, patch_size: list[int]) -> None: ...
    def set_N2V2(self, use_n2v2: bool) -> None: ...
    def set_N2V2_strategy(self, strategy: Literal['uniform', 'median']) -> None: ...
    def set_structN2V_mask(self, mask_axis: Literal['horizontal', 'vertical', 'none'], mask_span: int) -> None: ...
