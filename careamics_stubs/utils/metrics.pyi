import numpy as np
import torch
from _typeshed import Incomplete

def psnr(gt: np.ndarray, pred: np.ndarray, data_range: float) -> float: ...
def scale_invariant_psnr(gt: np.ndarray, pred: np.ndarray) -> float | torch.tensor: ...

class RunningPSNR:
    N: Incomplete
    mse_sum: Incomplete
    max: Incomplete
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    min: Incomplete
    def update(self, rec: torch.Tensor, tar: torch.Tensor) -> None: ...
    def get(self) -> torch.Tensor | None: ...

def multiscale_ssim(gt_: np.ndarray | torch.Tensor, pred_: np.ndarray | torch.Tensor, range_invariant: bool = True) -> list[float | None]: ...
def avg_range_inv_psnr(target: np.ndarray, prediction: np.ndarray) -> float: ...
def avg_psnr(target: np.ndarray, prediction: np.ndarray) -> float: ...
def avg_ssim(target: np.ndarray | torch.Tensor, prediction: np.ndarray | torch.Tensor) -> tuple[float, float]: ...
