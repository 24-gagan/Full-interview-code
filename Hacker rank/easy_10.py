if __name__=="__main__":
    n=int(input())
    students_marks={}
    for _ in range(n):
        name,*line=input().split()
        scores=list(map(float,line))
        students_marks[name]=scores
    query_name=input()
    mark_avg=sum(students_marks[query_name])/3
    print(f'{marks_avg:.2f}')