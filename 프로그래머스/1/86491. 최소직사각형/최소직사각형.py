def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
        longer = max(w, h)
        shorter = min(w, h)

        if longer > max_w:
            max_w = longer

        if shorter > max_h:
            max_h = shorter

    return max_w*max_h