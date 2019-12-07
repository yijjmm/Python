def check_id(message):
    if message.isdigit() or message.isalpha(): # if <message> only digit or alphabet
        print("아이디는 문자와 숫자가 같이 포함되어야 합니다")

def generate_password():
    import random
    return ''.join([chr(random.randint(ord('a'), ord('z'))) for i in range(6)])

def display_member(member):
    for j in range(2):
        print()
        print("아이디 : ", d[j][0])
        print("비밀번호 : ", generate_password())
        print("추가정보 : ", d[j][1], d[j][2]) # (weight, height)

d = []

for i in range(2):
    lst = []
    user_id = input("아이디 입력 : ")
    lst.append(user_id)
    height = int(input("신장 입력 : "))
    lst.append(height)
    weight = float(input("몸무게 입력 : "))
    lst.append(weight)
    d.append(lst)

display_member(d)
