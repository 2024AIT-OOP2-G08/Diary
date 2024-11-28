from IkedaDiary import IkedaDiary
from MisakiDiary import MisakiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    MisakiDiary(),
    IkedaDiary(),
    ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()