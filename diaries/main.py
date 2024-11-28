
from DiarySample import DiarySample
from ToriiDiary import ToriiDiary
from IkedaDiary import IkedaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), ToriiDiary(), IkedaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()