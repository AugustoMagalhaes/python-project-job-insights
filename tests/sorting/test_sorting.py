from src.sorting import sort_by


def test_sort_by_criteria():
    all_jobs = [
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
    ]

    expected_sort_by_max_salary = [
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
    ]

    invalid_sort_by_max_salary = [
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
    ]

    expected_sort_by_min_salary = [
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
    ]

    invalid_sort_by_min_salary = [
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
    ]

    expected_sort_by_date_posted = [
      {"min_salary": 1200, "date_posted": "2022-11-13"},
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
    ]

    invalid_sort_by_date_posted = [
      {"max_salary": None, "min_salary": 1200, "date_posted": "2022-11-11"},
      {"min_salary": 1200, "date_posted": "2022-11-13"},
      {"max_salary": 1900, "min_salary": 1200, "date_posted": "2022-01-01"},
      {"max_salary": 1200, "min_salary": 1000, "date_posted": "2022-11-10"},
    ]

    sort_by(all_jobs, "max_salary")
    assert all_jobs == expected_sort_by_max_salary
    assert all_jobs != invalid_sort_by_max_salary

    sort_by(all_jobs, "min_salary")
    assert all_jobs == expected_sort_by_min_salary
    assert all_jobs != invalid_sort_by_min_salary

    sort_by(all_jobs, "date_posted")
    assert all_jobs == expected_sort_by_date_posted
    assert all_jobs != invalid_sort_by_date_posted
