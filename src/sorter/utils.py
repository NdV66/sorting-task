from .consts import SEPARATOR
from functools import cmp_to_key
import os
from utils import file


def sort_data(a, b):
    if a[1] < b[1]:
        return -1
    if a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        return -1
    return 1


def map_data(data):
    parts = data.split(".")
    parts[0] = int(parts[0])
    return parts


def sort_data_when_merging(a, b):
    a = map_data(a)
    b = map_data(b)
    return sort_data(a, b)


def sort_chunk(data):
    data_in_parts = list(map(map_data, data))
    sorted_key = cmp_to_key(sort_data)
    data_in_parts.sort(key=sorted_key)
    return list(map(lambda x: str(x[0]) + SEPARATOR + x[1], data_in_parts))


def create_chunk(filename, chunk_data, base_path_for_chunks):
    data_file_path = os.path.join(base_path_for_chunks, filename)
    file.create_file_by_path(data_file_path, chunk_data)
