from zarr import Group as Group, core, hierarchy, storage

def read_zarr(zarr_source: Group, axes: str) -> core.Array | storage.DirectoryStore | hierarchy.Group: ...
