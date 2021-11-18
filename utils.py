def duration_in_millisec(records):
    duration = {}
    for g_id, millisec in records:
        if g_id in duration:
            duration[g_id] += millisec
        else:
            duration[g_id] = millisec
    return duration
