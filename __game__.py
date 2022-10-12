import random
import time
import pickle
from playsound import playsound


def game_start(words, play_repeat=11):
    accuracy = 0
    for __ in range(play_repeat):
        print(f"{__} 번째 게임을 시작합니다.")
        prob = random.sample(words, 1)[0]
        words.remove(prob)
        print(prob)
        pred = input('단어입력 :')
        if prob == pred:
            print("정답!")
            playsound('source/success.MP3', block=False)
            accuracy += 1
        elif prob != pred:
            print("오답!")
            playsound('source/wrong.MP3', block=False)
    return accuracy
