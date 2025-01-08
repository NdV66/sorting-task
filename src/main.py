import creator
import sorter
import os
import time

OUTPUT_FILENAME = "sample.txt"
SAMPLE_FINAL_SIZE_BYTES = 1024 * 100 * 7  # 700 7B
SAMPLE_FINAL_SIZE_BYTES = 1024 * 100
MAX_CHUNK_SIZE_B = 1024 / 10


def main():
    start_time = time.time()
    print("------ START CREATING ------")
    creator.create(OUTPUT_FILENAME, SAMPLE_FINAL_SIZE_BYTES)
    print("------ FINISH CREATING ------")

    print("------ START SORTING ------")
    data_file_path = os.path.join(os.getcwd(), "src", "creator", OUTPUT_FILENAME)
    sorter.do_sort(data_file_path, MAX_CHUNK_SIZE_B)

    seconds = time.time() - start_time
    file_size_Gb = SAMPLE_FINAL_SIZE_BYTES / 125000000
    final_minutes = seconds / 60
    print("--- %s Gb/minute ---" % (file_size_Gb / final_minutes))
    print("------ FINISH SORTING ------")


if __name__ == "__main__":
    main()
