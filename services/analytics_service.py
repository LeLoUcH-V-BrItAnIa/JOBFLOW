from services.job_service import get_all_jobs

def get_status_counts():

    jobs = get_all_jobs()

    counts = {
        "Applied": 0,
        "Assessment": 0,
        "Interview": 0,
        "HR Round": 0,
        "Accepted": 0,
        "Rejected": 0
    }

    for job in jobs:

        status = job.get("status")

        if status in counts:
            counts[status] += 1

    return counts