def study_schedule(permanence_period, target_time):
    arr = []
    for period in permanence_period:
        if filters(period, target_time) is None:
            return None

        if period[0] <= target_time <= period[1]:
            arr.append(True)

    return len(arr)


def filters(period, target_time):
    result = ''
    if isinstance(period[0], str) or isinstance(period[1], str)\
            or isinstance(target_time, tuple):
        result = None

    if not period[0] or not period[1] or not target_time:
        result = None

    return result
