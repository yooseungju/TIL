



def DFS(start, answer, visited):
    global stop, ans

    if stop:
        return
    if sum(visited) == len(tickets):
        ans = answer[::]
        stop = 1
        return
    for i in range(len(tickets)):
        if tickets[i][0] == start and not visited[i]:
            visited[i] = 1
            answer.append(tickets[i][1])
            DFS(tickets[i][1],answer,visited)
            answer.pop()
            visited[i] = 0


def solution(M):
    global tickets
    tickets = sorted(M , key = lambda x:x[1])
    visited = [0] * len(tickets)
    DFS('ICN', ['ICN'] ,visited)

    return ans



ans = 0
tickets = 0
stop = 0

a = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(a))


