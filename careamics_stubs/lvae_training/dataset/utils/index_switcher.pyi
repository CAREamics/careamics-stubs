from _typeshed import Incomplete

class IndexSwitcher:
    idx_manager: Incomplete
    def __init__(self, idx_manager, data_config, patch_size) -> None: ...
    def get_valid_target_index(self): ...
    def get_invalid_target_index(self): ...
    def get_valid_target_hw(self, t): ...
    def get_invalid_target_hw(self, t): ...
    def index_should_have_target(self, index): ...
    @staticmethod
    def get_reduced_frame_size(data_shape_nhw, fraction): ...
