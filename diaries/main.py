from IkedaDiary import IkedaDiary
from MisakiDiary import MisakiDiary
from ToriiDiary import ToriiDiary
from AsariDiary import AsariDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    MisakiDiary(),
    IkedaDiary(),
    ToriiDiary(),
    AsariDiary()
    ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()