def calculate_area(base_list, height_list):
    """ (list of numbers, list of numbers) -> list of floats
    
    precondition: len(base_list) == len(height_list)
    
    return a list of the triangle areas for triangles with a base in base_list and a height at height_list
    
    >>> calculate_area([10, 5, 7.5], [8, 5, 7.5])
    [40.0, 12.5, 28.125]
    """
    
    area_list = []
    i = 0
    while i < len(base_list):
        area_list.append(float(base_list[i] * height_list[i]) // 2)
        i = i + 1
    return area_list
            
            
            