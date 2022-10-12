import time
import sys
import warnings
from __scoredb__ import *
from __words__ import *
from __game__ import *

warnings.filterwarnings(action='ignore')

# db settings
connect,db_cursor = load_db()
score_table = db_cursor.fetchall()

# name checking
name_list=[i[0] for i in score_table]
user_name = input('your name for record!')
if is_samename(user_name,name_list=name_list):
    user_decision = input("you got same name in score_list (renew[re]/another_name[an])")
    if user_decision == 're':
        pass
    elif user_decision == 'an':
        user_name = input('new_name : ')

# game language
game_lang = input('Korean or English [kr/en]')
if game_lang == 'kr':
    trends = trends_retriever("KR")
    trend_writer(trends=trends, lang=game_lang)
elif game_lang == 'en':
    trends = trends_retriever("US")
    trend_writer(trends=trends, lang=game_lang)
words = read_word(game_lang)

# game start
start_time = time.time()
accuracy = game_start(play_repeat=11, words=words)
total_time = time.time() - start_time

# game information
print(f'당신의 자세한 결과>> 게임시간: {total_time}, 정답 수 : {accuracy}')
if accuracy >= 7:
    print('게임 통과!!!')
elif accuracy < 7:
    print('게임 실패!!!')
    playsound('source/finally_failed.MP3',block=False)

# record_check
if len(score_table)==0:
    print('지금은 등록된 사람이 없습니다!!! 당신이 처음 기록되었습니다.')
    user_data = (user_name, accuracy, total_time)
    save_score2db(data=user_data, cursor=db_cursor, connect=connect)
    sys.exit()

user_data = (user_name,accuracy,total_time)
save_score2db(data=user_data,cursor=db_cursor,connect=connect)

connect.close()
connect,db_cursor = load_db()
score_table = db_cursor.fetchall()

top_rates = sorted(score_table, key=lambda x:x[1], reverse=True)[:3]

for i, data in enumerate(top_rates):
    if user_name == data[0]:
        playsound('source/finally_did.MP3', block=True)
    print(f"{i + 1}등 이름 : {data[0]}, 맞힌문제수 : {data[1]}, 시간 : {data[2]}")