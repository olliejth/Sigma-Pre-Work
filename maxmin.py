def max_min(numbers):

    min_and_max = []
    max, min = numbers[0], numbers[0]

    for num in numbers:
        if num > max:
            max = num
        if num < min:
            min = num

    min_and_max.append(min)
    min_and_max.append(max)

    print(min_and_max)


max_min([100, -100])
