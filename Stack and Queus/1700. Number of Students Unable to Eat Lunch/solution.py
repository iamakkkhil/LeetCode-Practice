def countStudents(students, sandwiches) -> int:
    counter = 0

    while len(students):
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            counter = 0
        else:
            counter += 1
            students.append(students.pop(0))

        if counter >= len(students):
            break

    return len(students)


if __name__ == "__main__":
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    print(countStudents(students, sandwiches))
