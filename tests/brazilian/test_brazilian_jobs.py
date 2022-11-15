from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    br_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in br_jobs:
        assert "title" in job.keys()
        assert "titulo" not in job.keys()
        assert "salary" in job.keys()
        assert "salario" not in job.keys()
        assert "type" in job.keys()
        assert "tipo" not in job.keys()
