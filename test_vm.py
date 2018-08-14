from vm import run, init
# 각 test는 독립적으로 실행되어야 한다.


def test_initial_change():
    init()
    assert "잔액은 0원입니다." == run("잔액")

def test_insert_coin_and_check():
    init()
    assert "100원을 넣었습니다." == run("동전 100")
    assert "잔액은 100원입니다." == run ("잔액")

def test_accumalation_of_change():
    init()
    run("동전 100")
    run("동전 100")
    assert "잔액은 200원입니다." == run ("잔액")

def test_unknown_command():
    init()
    assert "알 수 없는 명령입니다." == run("blah")
