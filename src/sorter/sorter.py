import os
from uuid import uuid4
from numpy import setdiff1d
from .split_into_files import split_into_files
from .consts import BASE_PATH_FOR_CHUNKS, CHUNK_EXTENSION, CHUNK_FILE_NAME
from .utils import sort_data_when_merging, create_chunk


def do_k_merge_sort(current_files):
    i = 0
    merged_chunk_prefix = str(uuid4()) + "_"
    current_files_len = len(current_files)
    filenames_to_remove = []

    while current_files_len > 1:
        if i + 1 >= current_files_len:
            i = 0
            merged_chunk_prefix = str(uuid4()) + "_"
            current_files = setdiff1d(current_files, filenames_to_remove).tolist()
            current_files_len = len(current_files)
            print("------ ------ ------ ------ ------" + "--> next files amount: " + str(current_files_len))
            continue

        source_filename_1 = current_files[i]
        source_filename_2 = current_files[i + 1]
        source_path_1 = os.path.join(BASE_PATH_FOR_CHUNKS, source_filename_1)
        source_path_2 = os.path.join(BASE_PATH_FOR_CHUNKS, source_filename_2)
        merged_filename = merged_chunk_prefix + str(i) + CHUNK_EXTENSION

        with open(source_path_1, "r") as source_1, open(source_path_2, "r") as source_2:
            line_source_1 = source_1.readline()
            line_source_2 = source_2.readline()

            while line_source_1 and line_source_2:
                result = sort_data_when_merging(line_source_1, line_source_2)

                if result == -1:
                    create_chunk(merged_filename, line_source_1, BASE_PATH_FOR_CHUNKS)
                    line_source_1 = source_1.readline()
                else:
                    create_chunk(merged_filename, line_source_2, BASE_PATH_FOR_CHUNKS)
                    line_source_2 = source_2.readline()

            while line_source_1:
                create_chunk(merged_filename, line_source_1, BASE_PATH_FOR_CHUNKS)
                line_source_1 = source_1.readline()

            while line_source_2:
                create_chunk(merged_filename, line_source_2, BASE_PATH_FOR_CHUNKS)
                line_source_2 = source_2.readline()

        current_files.append(merged_filename)
        filenames_to_remove.append(source_filename_1)
        filenames_to_remove.append(source_filename_2)
        i += 2

    return current_files[0]


def do_sort(data_file_path, file_max_size):
    max_chunk_index = split_into_files(data_file_path, file_max_size, CHUNK_FILE_NAME)
    start_files = [CHUNK_FILE_NAME + str(i) + CHUNK_EXTENSION for i in range(0, max_chunk_index + 1)]
    result = do_k_merge_sort(start_files)
    print("RESULT: " + result)
