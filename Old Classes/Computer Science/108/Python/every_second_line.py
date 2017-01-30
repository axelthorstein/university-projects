def every_second_line(report):
    """ (Open File for reading) -> list of str
    
    Return a list containing every second line (with leading and trailing
    whitespace removed) in report, starting with the first line.
    """
    f = report
    
    result = []
    for line in f:
        result.append(line.strip())
        f.readline()
        