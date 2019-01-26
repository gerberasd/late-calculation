
import time

print("まずは定数を入力して下さい。")
teisuu = input()
teisuu = float(teisuu)

print("次に譜面スコアを入力して下さい。")
score = input()
score = int(score)

if score >= 1007500:         
    reply = teisuu + 2
    print("\n",reply)
elif score >= 1005000:         
    reply = teisuu + 1.5 + ((score - 1005000) / 5000 )
    print("\n",reply)
elif score >= 1000000:         
    reply = teisuu + 1.0 + ((score - 1000000) / 10000)
    print("\n",reply)
elif score >= 975000:         
    reply = teisuu + ((score - 975000) / 25000)
    print("\n",reply)
elif score >= 950000:         
    reply = teisuu - 1.5 + ((score - 950000) / 50000)
    print("\n",reply)
elif score >= 925000:         
    reply = teisuu - 3.0 + ((score - 925000) / 50000)
    print("\n",reply)
elif score >= 900000:         
    reply = teisuu - 3.0 + ((score - 900000) / 25000)
    print("\n",reply)
else:        
    reply = 'BBB以下のスコアは計算できません。A以上のスコアを入力して下さい。'
    print("\n",reply)

print("\n10秒後に自動的に閉じます")

time.sleep(10)