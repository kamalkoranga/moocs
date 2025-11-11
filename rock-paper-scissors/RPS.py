wtf = {}

def player(prev_play, opponent_history:list[str]=[]) -> str:
  global wtf

  n:int = 5

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess:str = "R"

  if len(opponent_history) > n:
    inp:str = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in wtf.keys():
      wtf["".join(opponent_history[-(n+1):])]+=1
    else:
      wtf["".join(opponent_history[-(n+1):])]=1

    possible:list[str] = [inp+"R", inp+"P", inp+"S"]

    for i in possible:
      if not i in wtf.keys():
        wtf[i] = 0

    predict:str = max(possible, key=lambda key: wtf[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess
