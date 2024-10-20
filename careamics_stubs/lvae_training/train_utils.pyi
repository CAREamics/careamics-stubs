import ml_collections
from _typeshed import Incomplete

def log_config(config: ml_collections.ConfigDict, cur_workdir: str) -> None: ...
def set_logger(workdir: str) -> None: ...
def get_new_model_version(model_dir: str) -> str: ...
def get_model_name(config: ml_collections.ConfigDict) -> str: ...
def get_workdir(config: ml_collections.ConfigDict, root_dir: str, use_max_version: bool, nested_call: int = 0): ...
def get_mean_std_dict_for_model(config, train_dset): ...

class MetricMonitor:
    metric: Incomplete
    def __init__(self, metric) -> None: ...
    def mode(self): ...
