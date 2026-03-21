correct_username = "wzw"
correct_password = "123"

while True:
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if not username or not password:
        print("请再试")
        continue

    if username == correct_username and password == correct_password:
        print("恭喜登录成功")
        break
    else:
        print("请再试")
