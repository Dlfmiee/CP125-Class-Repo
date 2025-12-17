# Scenario 2
print(f"---- Scenario 2 ----")
      
scores = [ 78,82,79,81,80]
def has_distinction(scores):
    for item in scores:
        if item < 80:
            return False
    return True

print (has_distinction(scores))

#Scenario 5
print(f"---- Scenario 5 ----")

team_a = [ 3,2,1,4,2]
team_b = [ 2,2,3,1,2]

def compare_teams(team_a, team_b):
    Wins = 0
    Lose = 0
    Draw = 0

    for i in range(len(team_a)):
        if team_a[i] > team_b[i]:
            Wins += 1
        elif team_a[i] < team_b[i]:
            Lose += 1
        else:
            Draw += 1
    return [Wins, Lose, Draw]

print (compare_teams(team_a, team_b))