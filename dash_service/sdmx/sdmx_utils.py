def parse_data_query(dq: str) -> list:
    if dq is None:
        return []
    dq = dq.strip()
    ret = dq.split(".")
    for i in range(len(ret)):
        ret[i] = ret[i].split("+")
        ret[i] = [c for c in ret[i] if c!=""]

    return ret
