
if __name__ == '__main__':
2
    n = int(input())
3
    student_marks = {}
4
​
5
    for _ in range(n):
6
        line = input().split()
7
        name = line[0]
8
        scores = list(map(float, line[1:]))
9
        student_marks[name] = scores
10
​
11
    query_name = input()
12
​
13
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
14
    print("{:.2f}".format(average))
15
​