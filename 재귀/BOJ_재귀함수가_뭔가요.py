from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def recusive(level:int)->None:
    space = "_"* (4*level)
    if level==n:
        write(space+q1+"\n") # 재귀함수가 뭔가요 질문
        write(space+a1+"\n") # 재귀함수가 뭔가요 답변
        write(space+a2+"\n") # 재귀함수가 뭔가요 답변
        return

    write(space+q1+"\n") # 재귀함수가 뭔가요 질문
    write(space+q2+"\n") # 재귀함수가 뭔가요 질문
    write(space+q3+"\n") # 재귀함수가 뭔가요 질문
    write(space+q4+"\n") # 재귀함수가 뭔가요 질문
    recusive(level+1)
    write(space+a2+"\n")

n=int(input())

q1="\"재귀함수가 뭔가요?\""
q2="\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
q3="마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
q4="그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
a1="\"재귀함수는 자기 자신을 호출하는 함수라네\""
a2="라고 답변하였지."
write("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."+"\n")
recusive(0)
