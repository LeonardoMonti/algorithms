def study_schedule(permanence_period, target_time):
    try:
        result = None
        if target_time is not None:
            result = 0
            for period in permanence_period:
                if period[0] <= target_time <= period[1]:
                    result += 1
        return result

    except TypeError:
        return None
