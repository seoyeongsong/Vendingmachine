from vm import VendingMachine
# 각 test는 독립적으로 실행되어야 한다.


def test_initial_change():
    #init()
    m = VendingMachine()
    assert "잔액은 0원입니다." == m.run("잔액")

def test_insert_coin_and_check():
    # init()
    m = VendingMachine()
    assert "100원을 넣었습니다." == m.run("동전 100")
    assert "잔액은 100원입니다." == m.run ("잔액")

def test_accumalation_of_change():
    # init()
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다." == m.run ("잔액")

def test_unknown_command():
    # init()
    m = VendingMachine()
    assert "알 수 없는 명령입니다." == m.run("blah")

def test_give_me_coffee():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피" == m.run("음료 커피")

def test_unknown_coin():
    m = VendingMachine()
    assert "알 수 없는 동전입니다." == m.run("동전 230")
