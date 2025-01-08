from random import randint
from .texts import RANDOM_TEXTS, RANDOM_TEXT_LEN
import os
from utils import file

HOW_MANY_FILES = 10
HOW_MANY_LINES_IN_FILE = 1000
MIN_RANDOM = 0
MAX_RANDOM = 10000
END_LINE_SIZE_BYTES = 2
BASE_PATH_FOR_CHUNKS = os.path.join(os.getcwd(), "src", "creator")


def prepare_data_one_line(min, max):
    number = randint(min, max)
    text_index = randint(0, RANDOM_TEXT_LEN - 1)
    return str(number) + "." + RANDOM_TEXTS[text_index]


def create(output_filename, sample_final_size_bytes):
    data_file_path = os.path.join(BASE_PATH_FOR_CHUNKS, output_filename)
    file.create_file_by_path(data_file_path, "")
    current_size = file.get_file_size_bytes(__file__, output_filename)

    if current_size > 0:
        file.remove_file_by_path(data_file_path)
        current_size = 0

    while current_size < sample_final_size_bytes:
        line = prepare_data_one_line(MIN_RANDOM, MAX_RANDOM)
        size_diff_bytes = int(sample_final_size_bytes - current_size)
        line_len = len(line)

        if size_diff_bytes < line_len:
            line = line[:size_diff_bytes]

        if size_diff_bytes > 3:
            next_size = current_size + line_len + END_LINE_SIZE_BYTES >= sample_final_size_bytes
            if not next_size:
                line += "\n"
                line_len += END_LINE_SIZE_BYTES

        file.create_file_by_path(data_file_path, line)
        # 1 byte == 1 character
        current_size += line_len

    current_size = file.get_file_size_bytes(__file__, output_filename)
    print(f"Final size: {current_size} bytes, expected: {sample_final_size_bytes} bytes: {sample_final_size_bytes == current_size}")
