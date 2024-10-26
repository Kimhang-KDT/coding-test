#문제 설명
#덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

#제한사항
#연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.
#1 ≤ quiz의 길이 ≤ 10
#X, Y, Z는 각각 0부터 9까지 숫자로 이루어진 정수를 의미하며, 각 숫자의 맨 앞에 마이너스 기호가 하나 있을 수 있고 이는 음수를 의미합니다.
#X, Y, Z는 0을 제외하고는 0으로 시작하지 않습니다.
#-10,000 ≤ X, Y ≤ 10,000
#-20,000 ≤ Z ≤ 20,000
#[연산자]는 + 와 - 중 하나입니다.

def solution(quiz):
    answer = []
    # quiz를 공백 기준으로 따로 담을 배열 필요
    arrs = [i.split(" ") for i in quiz]
    
    for arr in arrs:
        # arr[0], arr[2], arr[4]는 무조건 숫자
        # arr[1]은 연산자, + - 만 존재
        num = int(arr[4])
        
        plus = int(arr[0]) + int(arr[2])
        minus = int(arr[0]) - int(arr[2])
        
        # answer에는 O와 X만 담을것
        if arr[1] == "+":
            answer.append('O' if plus == num else 'X')
        else:
            answer.append('O' if minus == num else 'X')
    
    return answer