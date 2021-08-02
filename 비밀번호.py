pw="강민 천제"
input_pw=input("비밀번호:")
if input_pw==pw:
    print("환영합니다!")
    new_pw=input("new password:")
    print("이전 비밀번호: {}".format(pw))
    print("new password:{}".format(new_pw))
    pw=new_pw
else:
    print("who are you")
print("방문에 주셔서 감사")
