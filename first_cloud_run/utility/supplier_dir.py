import os


def get_batch_dir(batch_dir: str):
    has_supplier_dir = os.path.exists(batch_dir)
    if not has_supplier_dir:
        os.makedirs(batch_dir)
    return batch_dir
