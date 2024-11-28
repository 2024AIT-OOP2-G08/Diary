from DiarySample import DiarySample
from diaries.ToriiDiary import ToriiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), ToriiDiary(),]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()