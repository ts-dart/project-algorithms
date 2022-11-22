def study_schedule(permanence_period, target_time):
    arr, result = [], ''
    for period in permanence_period:
        if isinstance(period[0], str) or isinstance(period[1], str)\
                or isinstance(target_time, tuple):
            result = None

        if not period[0] or not period[1] or not target_time:
            result = None

        if result is None:
            return result

        if period[0] <= target_time <= period[1]:
            arr.append(True)

    return len(arr)
