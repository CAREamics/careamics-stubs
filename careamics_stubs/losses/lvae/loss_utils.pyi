import torch

def free_bits_kl(kl: torch.Tensor, free_bits: float, batch_average: bool = False, eps: float = 1e-06) -> torch.Tensor: ...
def get_kl_weight(kl_annealing: bool, kl_start: int, kl_annealtime: int, kl_weight: float, current_epoch: int) -> float: ...
