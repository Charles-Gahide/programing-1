from math import floor


def thanos(queue_size, target_size):
    snaps_needed = 0

    # Loop until the queue size is less than or equal to the target size
    while queue_size > target_size:
        queue_size=floor(queue_size/2)
        snaps_needed += 1

    return (snaps_needed)

thanos(100, 25)
thanos(50, 4)