import os

def prepare_filename(dirname, file_name):
    main_path = os.path.dirname(dirname)
    return os.path.join(main_path, file_name)

def create_file(dirname, file_name, data):
    data_file_path = prepare_filename(dirname, file_name)
    file = open(data_file_path, 'a+')
    file.write(data)
    file.close()

def open_file(dirname, file_name, permissions = "r"):
    data_file_path = prepare_filename(dirname, file_name)
    return open(data_file_path, permissions)
    

def remove_file(dirname, file_name):
    data_file_path = prepare_filename(dirname, file_name)
    os.remove(data_file_path)