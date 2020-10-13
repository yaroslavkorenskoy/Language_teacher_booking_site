import json


def write_json_file(path, data, indent=4, encoding='utf-8'):
    with open(path, 'w', encoding=encoding) as fd:
        json.dump(data, fd, indent=indent, ensure_ascii=False)


def read_json_file(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding) as fd:
        return json.load(fd)
