import torch
from careamics.losses.loss_factory import LVAELossParameters as LVAELossParameters
from careamics.losses.lvae.loss_utils import free_bits_kl as free_bits_kl, get_kl_weight as get_kl_weight
from careamics.models.lvae.likelihoods import GaussianLikelihood as GaussianLikelihood, LikelihoodModule as LikelihoodModule, NoiseModelLikelihood as NoiseModelLikelihood
from careamics.models.lvae.utils import compute_batch_mean as compute_batch_mean
from typing import Any

Likelihood = LikelihoodModule | GaussianLikelihood | NoiseModelLikelihood

def get_reconstruction_loss(reconstruction: torch.Tensor, target: torch.Tensor, likelihood_obj: Likelihood) -> dict[str, torch.Tensor]: ...
def reconstruction_loss_musplit_denoisplit(predictions: torch.Tensor | tuple[torch.Tensor, torch.Tensor], targets: torch.Tensor, nm_likelihood: NoiseModelLikelihood, gaussian_likelihood: GaussianLikelihood, nm_weight: float, gaussian_weight: float) -> torch.Tensor: ...
def get_kl_divergence_loss_usplit(topdown_data: dict[str, list[torch.Tensor]], img_shape: tuple[int] = (64, 64), kl_key: str = 'kl') -> torch.Tensor: ...
def get_kl_divergence_loss_denoisplit(topdown_data: dict[str, torch.Tensor], img_shape: tuple[int], kl_key: str = 'kl') -> torch.Tensor: ...
def musplit_loss(model_outputs: tuple[torch.Tensor, dict[str, Any]], targets: torch.Tensor, loss_parameters: LVAELossParameters) -> dict[str, torch.Tensor] | None: ...
def denoisplit_loss(model_outputs: tuple[torch.Tensor, dict[str, Any]], targets: torch.Tensor, loss_parameters: LVAELossParameters) -> dict[str, torch.Tensor] | None: ...
def denoisplit_musplit_loss(model_outputs: tuple[torch.Tensor, dict[str, Any]], targets: torch.Tensor, loss_parameters: LVAELossParameters) -> dict[str, torch.Tensor] | None: ...
