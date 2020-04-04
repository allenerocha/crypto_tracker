"""This module iterates over a directory and subsequent subdirectories to read the json files in the subdirectories"""
import tqdm
import time
import os
import json


def parse(path: str) -> dict:
    """
    This funtion iterates over the given path and directories in that path to read the json data files
    :param path: path to iterate over
    :return: dictionary of all the data in the files
    """
    total_time = time.time()

    data = dict()

    dir_count = 0
    file_count = 0

    for directory in tqdm.tqdm(os.listdir(f"{path}")):
        for filename in tqdm.tqdm(os.listdir(f"{path}/{directory}")):
            try:
                json_data = json.loads(open(f"data/{directory}/{filename}").read())
                data[f"{directory}-{filename}".replace(".json", "")] = json_data
                file_count += 1
            except json.decoder.JSONDecodeError as e:
                print(f"data/{directory}/{filename}\n{str(e)}")
        dir_count += 1

    if dir_count == 1:
        print(f"Added {file_count} files in {time.time() - total_time} seconds from {dir_count} directory")
    else:
        print(f"Added {file_count} files in {time.time() - total_time} seconds from {dir_count} directories")
    return data

