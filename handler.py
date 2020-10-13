import os

from utils import write_json_file, read_json_file


def update_data(path, new_data: dict):
    if not (os.path.exists(path) and os.path.isfile(path)):
        write_json_file(path, data=[])

    data_list = read_json_file(path)
    data_list.append(new_data)
    write_json_file(path, data_list)
