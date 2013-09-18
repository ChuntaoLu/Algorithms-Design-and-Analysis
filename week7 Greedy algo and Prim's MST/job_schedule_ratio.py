def weighted_complete_time(jobs):
    """Greedy algorithm for job completion time by scheduling jobs
    base on ratio (weight / length), returns weighted total time."""
    
    sorted_jobs = ratio_sort(jobs)
    complete_time = time_to_complete(sorted_jobs)
    total_time = sum([i[0] * i[1] for i in complete_time])
    return total_time


def ratio_sort(jobs):
    """Sort jobs by the ration of (weight / length)."""

    ratio_jobs = [i + [float(i[0]) / i[1]] for i in jobs]
    sorted_jobs = sorted(ratio_jobs, key=lambda job: job[-1], reverse=True)
    return sorted_jobs


def time_to_complete(jobs):
    """Calculate the finish time for each job in the job schedule, and
    update the current_complete_time."""

    current_complete_time = 0
    for job in jobs:
        job[1] += current_complete_time
        current_complete_time = job[1]
    return jobs


def main():
    jobs = []
    with open('jobs.txt') as file_in:
    #with open('test2.txt') as file_in:
        next(file_in) #start reading from line 2
        for line in file_in:
            jobs.append(map(int, line.strip().split(' ')))
    return weighted_complete_time(jobs)


if __name__ == '__main__':
    print main()
