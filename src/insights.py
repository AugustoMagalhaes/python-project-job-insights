import src.jobs


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    all_jobs = src.jobs.read(path)
    filtered_jobs = []
    for job in all_jobs:
        if not job["job_type"] in filtered_jobs:
            filtered_jobs.append(job["job_type"])
    return filtered_jobs


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    matching_jobs_types = [job for job in jobs if job["job_type"] == job_type]
    return matching_jobs_types


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_industries = src.jobs.read(path)
    filtered_industries = []
    for job in all_industries:
        if not job["industry"] in filtered_industries and job["industry"]:
            filtered_industries.append(job["industry"])
    return filtered_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    matching_jobs_industries = (
      [job for job in jobs if job["industry"] == industry]
      )
    return matching_jobs_industries


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = src.jobs.read(path)
    all_max_salaries = []
    for job in data:
        if job["max_salary"].isnumeric():
            all_max_salaries.append(int(job["max_salary"]))

    max_salary = sorted(all_max_salaries, reverse=True)[0]
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = src.jobs.read(path)
    all_min_salaries = []
    for job in data:
        if job["min_salary"].isnumeric():
            all_min_salaries.append(int(job["min_salary"]))

    min_salary = sorted(all_min_salaries)[0]
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
