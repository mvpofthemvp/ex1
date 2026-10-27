import math

def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Vector dimensions must match")
    
    return math.sqrt(
        sum((x-y) ** 2 for x,y in zip(a,b))
    )

def classify_vector(query, group_a, group_b):
    if not group_a or not group_b:
        raise ValueError("Groups cannot be empty")
    distances_a = [
        euclidean_distance(query, vector)
        for vector in group_a
    ]
    distances_b = [
        euclidean_distance(query, vector)
        for vector in group_b
    ]

    avg_a = sum(distances_a) / len(distances_a)
    avg_b = sum(distances_b) / len(distances_b)

    return 0 if avg_a <= avg_b else 1


group_a = [
    [0.9, 0.1, 0.2],
    [0.8, 0.2, 0.1],
    [0.95, 0.1, 0.15]
]
group_b = [
    [0.1, 0.9, 0.2],
    [0.2, 0.8, 0.1],
    [0.1, 0.95, 0.15]
]

query_vector = [0.85, 0.15, 0.2]

result = classify_vector(query_vector, group_a, group_b)
print(result)


