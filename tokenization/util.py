import os


def create_dirs(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
