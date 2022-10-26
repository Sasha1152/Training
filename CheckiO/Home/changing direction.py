def changing_direction(elements: list) -> int:
    vectors = []
    for i in range(1, len(elements)):
        if elements[i] > elements[i-1]:
            vectors.append(1)
        elif elements[i] < elements[i-1]:
            vectors.append(-1)

    status = 0
    for i in range(1, len(vectors)):
        if vectors[i] != vectors[i-1]:
            status += 1

    return status


print(changing_direction([1, 2, 3, 4, 5]))
print(changing_direction([5, 4, 3, 2, 1]))
print(changing_direction([1, 2, 3, 2, 1]))
print(changing_direction([1, 2, 2, 1, 2, 2]))
