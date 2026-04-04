# logic.py
from typing import List, Dict

# 牌值權重表
CARD_VALUES = {
    "A": -5, "2": -4, "3": -3, "4": -2, "5": 1,
    "6": 2, "7": 3, "8": 4, "9": 5,
    "10": 0, "J": 0, "Q": 0, "K": 0
}

# AP 優勢權重表
AP_VALUES = {
    0: 0.5,
    1: 0.4,
    2: 0.3,
    3: 0.3,
    4: 0.1,
    5: 0.2,
    6: 0.3,
    7: 0.3,
    8: 0.5,
    9: 0.1
}

history: List[Dict] = []

def calc_cp(cards: List[str]) -> int:
    """計算 CP 值 (牌值權重總和)"""
    return sum(CARD_VALUES.get(c.upper(), 0) for c in cards)

def calc_point(cards: List[str]) -> int:
    """計算點數 (總和 % 10)"""
    total = 0
    for c in cards:
        if c.upper() in ["10", "J", "Q", "K"]:
            val = 0
        else:
            val = int(c) if c.isdigit() else {"A":1}.get(c.upper(), 0)
        total += val
    return total % 10

def predict(code: Dict[str, List[str]]):
    """
    code = {
      "player": ["8", "J"],
      "banker": ["8", "9"]
    }
    """
    player_cp = calc_cp(code["player"])
    banker_cp = calc_cp(code["banker"])

    total_cp = player_cp + banker_cp

    player_point = calc_point(code["player"])
    banker_point = calc_point(code["banker"])

    player_ap = AP_VALUES[player_point]
    banker_ap = AP_VALUES[banker_point]

    player_adv = total_cp * player_ap
    banker_adv = total_cp * banker_ap

    if player_adv > banker_adv:
        suggestion = "Player"
    elif banker_adv > player_adv:
        suggestion = "Banker"
    else:
        suggestion = "Wait"

    record = {
        "player_cp": player_cp,
        "banker_cp": banker_cp,
        "total_cp": total_cp,
        "player_point": player_point,
        "banker_point": banker_point,
        "player_ap": player_ap,
        "banker_ap": banker_ap,
        "player_adv": player_adv,
        "banker_adv": banker_adv,
        "suggestion": suggestion
    }

    history.append(record)
    return record

def undo():
    if history:
        history.pop()
    return {"history_len": len(history)}

def reset():
    history.clear()
    return {"history_len": 0}
