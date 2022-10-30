import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    try:
        with open(path, encoding="utf-8") as csv_jobs:
            jobs_reader = csv.DictReader(
                csv_jobs, delimiter=",", quotechar='"'
            )
            jobs_list = list(jobs_reader)
            return jobs_list
    except FileExistsError:
        print("File does not exist")
