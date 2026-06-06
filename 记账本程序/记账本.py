import json
from datetime import datetime

FILE = "bill.json"

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("已保存")

def add(data):
    t = input("类型（收入/支出）：")
    m = float(input("金额："))
    n = input("备注：")
    data.append({
        "type": t,
        "money": m,
        "note": n,
        "time": datetime.now().strftime("%m-%d %H:%M")
    })
    print("添加成功")

def show(data):
    if not data:
        print("无记录")
        return
    for i, r in enumerate(data, 1):
        print(f"{i} {r['type']} {r['money']} {r['time']} {r['note']}")

def stat(data):
    in_ = sum(r["money"] for r in data if r["type"] == "收入")
    out = sum(r["money"] for r in data if r["type"] == "支出")
    print(f"收入: {in_} 支出: {out} 结余: {in_-out}")

data = load()
while True:
    print("\n1.添加 2.查看 3.统计 4.保存 0.退出")
    c = input("选择：").strip()
    if c == "1": add(data)
    elif c == "2": show(data)
    elif c == "3": stat(data)
    elif c == "4": save(data)
    elif c == "0":
        save(data)
        break
    else:
        print("无效选项")