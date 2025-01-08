from utils import file
from .consts import BASE_PATH_FOR_CHUNKS, START_CHUNK_INDEX, CHUNK_EXTENSION
from .utils import sort_chunk, create_chunk


def split_into_files(data_file_path, file_max_size, file_prefix):
    chunk_data = []
    chunk_index = START_CHUNK_INDEX
    original_file = file.open_file_by_path(data_file_path)

    with original_file as f:
        for line in f:
            filename = file_prefix + str(chunk_index) + CHUNK_EXTENSION

            if len(chunk_data) <= file_max_size:
                chunk_data.append(line)
            else:
                data = "".join(sort_chunk(chunk_data))
                create_chunk(filename, data, BASE_PATH_FOR_CHUNKS)
                chunk_data = []
                chunk_index += 1

        if chunk_data:
            data = "".join(sort_chunk(chunk_data))
            create_chunk(filename, data, BASE_PATH_FOR_CHUNKS)
            chunk_data = []

    original_file.close()
    return chunk_index
