# 감시 gold 4
# https://www.acmicpc.net/problem/15683
# 24-03-25  Python 3    38952 KB	1060 ms
#           PyPy3   	138796 KB	828 ms

from typing import List

MONITORED = -1
UNSEEN = 0
WALL = 6
INF = 65


class Cctv:
    def __init__(self, row: int, col: int, num: int) -> None:
        self.num = num
        self.row = row
        self.col = col
        self.dir = 0

    def turn(self) -> None:
        self.dir = (self.dir + 1) % 4

    def undo(self) -> None:
        self.dir = (self.dir - 1) % 4

    def watch(self, dir: int, room: List[List[int]]) -> List[List[int]]:
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]
        nr = self.row
        nc = self.col
        while True:
            nr += dr[dir]
            nc += dc[dir]
            if (
                nr < 0
                or nr >= len(room)
                or nc < 0
                or nc >= len(room[0])
                or room[nr][nc] == WALL
            ):
                break
            if room[nr][nc] != UNSEEN:
                continue
            room[nr][nc] = MONITORED
        return room

    def monitor(self, room: List[List[int]]) -> List[List[int]]:
        monitored_room = [
            [room[r][c] for c in range(len(room[0]))] for r in range(len(room))
        ]
        monitored_room = self.watch(self.dir, monitored_room)
        if self.num > 2:
            monitored_room = self.watch((self.dir + 1) % 4, monitored_room)
        if self.num != 1 and self.num != 3:
            monitored_room = self.watch((self.dir + 2) % 4, monitored_room)
        if self.num == 5:
            monitored_room = self.watch((self.dir + 3) % 4, monitored_room)
        return monitored_room


def solution():
    answer = INF
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    cctvs = [
        Cctv(r, c, office[r][c])
        for r in range(N)
        for c in range(M)
        if office[r][c] != UNSEEN and office[r][c] != WALL
    ]

    def simulate(idx: int, room: List[List[int]]):
        nonlocal answer
        if idx == len(cctvs):
            monitored = 0
            [
                monitored := monitored + 1
                for r in range(N)
                for c in range(M)
                if room[r][c] == UNSEEN
            ]
            answer = min(monitored, answer)
            return
        for i in range(4):
            monitored_room = cctvs[idx].monitor(room)
            simulate(idx + 1, monitored_room)
            if cctvs[idx].num == 5 or (cctvs[idx].num == 2 and i >= 2):
                break
            cctvs[idx].turn()
        return

    simulate(0, office)
    return print(answer)


solution()
