#%%

# load_ext nb_mypy

import mypy

from typing import List
Vector = List[float]

def add(v: Vector, u: Vector) -> Vector:
    assert len(v) == len(u), 'vectors must be the same length'

    return [v_i + u_i for v_i, u_i in zip(v, u)]

assert add([1, 2, 3], [2, 3, 4]) == [3, 5, 7], 'code is ok' 

def substract(v: List[float], u: List[float]) -> List[float]:
    assert len(v) == len(u), 'vectors must be the same lenght'

    return [v_i - u_i for v_i, u_i in zip(v, u)]

assert substract([5, 6, 7], [1, 2, 3]) == [4, 4, 4], 'answer is not correct'

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, 'no vectors provided'

    num_elements = len(vectors[0])
    assert all(num_elements == len(x) for x in vectors), 'different sizes'

    return [sum(vector[i] for vector in vectors) 
    for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6]]) == [9, 12]