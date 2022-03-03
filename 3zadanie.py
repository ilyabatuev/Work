with open(file="task_3_users.csv", mode="r", encoding="utf-8") as user_name:
    user_list = []
    for line in user_name:
        user_list.append(line)
with open(file="task_3_hobby.csv", mode="r", encoding="utf-8") as user_hobby:
    hobby_list = []
    for line in user_hobby:
        hobby_list.append(line)

hobby_username = dict()

def hobby_user():
    i = 0
    j = 0
    while i < len(user_list):
        if i >= len(hobby_list):
            hobby_username[user_list[j]] = None
            i += 1
            j += 1
            break
        else:
            hobby_username[user_list[j]] = hobby_list[i]
            i += 1
            j += 1

user_list = [line.rstrip() for line in user_list]
hobby_list = [line.rstrip() for line in hobby_list]
hobby_user()
print(hobby_username)


