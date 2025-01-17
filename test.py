import random

com_num = []
user_num = []
game_level = 0
game_cnt = 0

user_info = {
    '1_win' : 0,
    '1_lose' : 0,
    '2_win' : 0,
    '2_lose' : 0,
    '3_win' : 0,
    '3_lose' : 0,
    '4_win' : 0,
    '4_lose' : 0,
}

def start_game():
    print('게임을 시작합니다...')
    global com_num, game_level, game_cnt, user_info
    set_com_num()
    while True:
        set_result = set_user_num()
        if set_result.lower() != 'q':
            result = compair_num()
            if result['strike'] == 3 or game_cnt <= 0:
                com_num = []
                if game_cnt <= 0:
                    print('GAME OVER..')
                    user_info[str(game_level) + '_lose'] += 1
                else:
                    print('GAME WIN!!')
                    user_info[str(game_level) + '_win'] += 1
                break
            else:
                print(f'스트라이크 : {result['strike']} / 볼 : {result['ball']}')
        else:
            print('게임을 포기하셨습니다')
            user_info[str(game_level) + '_lose'] += 1
            com_num = []
            break

def show_my_info():
    global user_info
    print('-' * 50)
    print('내 전적 보기')
    print('-' * 50)
    for i in range(1, 5):
        if i == 1:
            print('쉬움')
        elif i == 2:
            print('보통')
        elif i == 3:
            print('어려움')
        elif i == 4:
            print('극한')
        print(f'승수 : {user_info[str(i) + '_win']}')
        print(f'패수 : {user_info[str(i) + '_lose']}')
        print('-' * 50)
    input_char = input('초기화 할까요?(y/n) : ')
    if input_char.lower() == 'y':
        for i in range(1,5):
            user_info[str(i) + '_win'] = 0
            user_info[str(i) + '_lose'] = 0

def set_com_num():
    print('컴퓨터 숫자 셋팅중....')
    global com_num
    com_cnt = 0
    while True:
        random_num = random.randint(0, 9)
        if not (random_num in com_num):
            com_num.append(random_num)
            com_cnt += 1
        if com_cnt >= 3:
            break
    print('컴퓨터 숫자 셋팅완료....')

def check_user_num():
    global user_num
    result_check = False
    if(len(user_num) != 3):
        print('입력하신 숫자가 3개가 아닙니다')
        return result_check

    for i in range(0, 3):
        try:
            user_num[i] = int(user_num[i])
        except:
            print('숫자가 아닌 글자가 있습니다')
            return result_check

        for j in range(0, 3):
            if i != j and user_num[i] == user_num[j]:
                print(f'i : {i} / j : {j} / user_num[i] : {user_num[i]} / user_num[j] = {user_num[j]}')
                print('중복된 숫자가 있습니다')
                return result_check

    result_check = True
    return result_check


def set_user_num():
    global user_num
    while True:
        check_yn = False
        input_user_num = input('세자리 숫자를 입력해주세요 (띄어쓰기로 구분 / 게임포기 : q) : ')

        if input_user_num.lower() == 'q':
            break

        user_num = input_user_num.split(' ')
        check_yn = check_user_num()
        if check_yn:
            break



    return input_user_num


def compair_num():
    global com_num, user_num, game_cnt
    result = { 'strike' : 0, 'ball' : 0}
    for i in range(0, 3):
        if user_num[i] == com_num[i] :
            result['strike'] += 1
        elif user_num[i] in com_num :
            result['ball'] += 1
    # 결과 구하고 나면 user_num 비워줌
    user_num = []
    game_cnt -= 1
    return result

def set_level():
    global game_cnt, game_level
    print('-' * 50)
    print('1. 쉬움')
    print('2. 보통')
    print('3. 어려움')
    print('4. 최악')
    print('-' * 50)

    while True:
        level = input('입력 : ')
        try:
            int(level)
        except:
            print('숫자를 입력해주세요')
            continue
        game_level = level
        level = int(level)
        if level == 1:
            game_cnt = 20
            break
        elif level == 2:
            game_cnt = 15
            break
        elif level == 3:
            game_cnt = 10
            break
        elif level == 4:
            game_cnt = 7
            break
        else:
            print('잘못된 입력입니다. 다시입력해주세요')


if __name__ == '__main__':
    while True:
        print('-' * 50)
        print('1. 게임시작')
        print('2. 내 전적 보기')
        print('3. 끝내기')
        print('-' * 50)

        input_num = input('입력 : ')
        try:
            int(input_num)
        except:
            print('숫자를 입력해주세요')
            continue
        input_num = int(input_num)
        if input_num == 1:
            set_level()
            start_game()
        elif input_num == 2 :
            show_my_info()
        elif input_num == 3 :
            break

