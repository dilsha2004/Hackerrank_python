def acmTeam(topics):
    n = len(topics)
    max_topics = 0
    max_teams = 0
    
    for i in range(n):
        for j in range(i+1, n):
    
            combined = int(topics[i], 2) | int(topics[j], 2)
            count = bin(combined).count('1')
            
            if count > max_topics:
                max_topics = count
                max_teams = 1
            elif count == max_topics:
                max_teams += 1
    
    return [max_topics, max_teams]
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    print(result)
    