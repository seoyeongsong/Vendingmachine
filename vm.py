change = 0

# class 설정하기
class VendingMachine:
    def __init__(self):
        self.change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]
        # params = tokens

        if cmd == "잔액":
            return "잔액은 " + str(self.change) + "원입니다."

        elif cmd == "동전":
            coin = params[0]
            if int(coin) not in [10, 50, 100, 500]:
                return "알 수 없는 동전입니다."
            self.change += int(coin)
            return coin + "원을 넣었습니다."

        elif cmd == "음료":
            if self.change >= 150:
                self.change = self.change - 150
                return "커피"
            else:
                return "잔액이 부족합니다."

        else:
            return "알 수 없는 명령입니다."


#
# def init():
#     global change
#     change = 0
#
#
#
# def run(raw):
#     global change
#
#
#     tokens = raw.split(" ")
#     cmd, params = tokens[0], tokens[1:]
#     # params = tokens
#
#
#     if cmd == "잔액":
#         return "잔액은 " + str(change) + "원입니다."
#     elif cmd == "동전":
#         coin = params[0]
#         change += int(coin)
#         return coin + "원을 넣었습니다."
#
#     else:
#         return "알 수 없는 명령입니다."
