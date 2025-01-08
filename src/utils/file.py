import os


def prepare_filename(origin_file, file_name):
    main_path = os.path.dirname(origin_file)
    return os.path.join(main_path, file_name)


def create_file_by_path(data_file_path, data):
    file = open(data_file_path, "a+")
    file.write(data)
    file.close()


def open_file_by_path(data_file_path, permissions="r"):
    return open(data_file_path, permissions)


def remove_file_by_path(data_file_path):
    os.remove(data_file_path)


def get_file_size_bytes(origin_file, file_name):
    data_file_path = prepare_filename(origin_file, file_name)
    return os.path.getsize(data_file_path)
