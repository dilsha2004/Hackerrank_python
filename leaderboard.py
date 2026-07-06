def climbingLeaderboard(ranked, player):
    scores = sorted(set(ranked), reverse=True)
    result = []
    index = len(scores) - 1
    for score in player:
        while index >= 0 and scores[index] <= score:
            index -= 1
        result.append(index + 2)   
    return result

if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print(result)