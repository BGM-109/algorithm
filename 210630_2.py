def solution(record):
    answer = []
    user = {}
    message = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    for i in record:
        arr = i.split()
        if arr[0] == 'Change' or arr[0] == 'Enter':
            user[arr[1]] = arr[2]

    for i in record:
        arr = i.split()
        if arr[0] == "Enter" or arr[0] == "Leave":
            str = ""
            str += user[arr[1]] + "님이 " + message[arr[0]]
            answer.append(str)

    return answer

# 오픈채팅방
