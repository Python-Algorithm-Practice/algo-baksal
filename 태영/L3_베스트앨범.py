# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    idx = []
    dict = {}

    # 인덱스, 장르, 재생횟수 순으로 배열에 추가
    for index, (i, j) in enumerate(zip(genres, plays)):
        idx.append([index, i, j])

    # 배열을 돌며 {장르 : 재생횟수} 형태의 딕셔너리 만듦
    for _, i, j in idx:
        dict[i] = dict.get(i, 0) + j

    # 재생횟수를 기준으로 정렬
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    # 장르, 재생횟수를 기준으로 정렬
    idx.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print(dict)
    print(idx)

    # 장르별로 노래를 두개씩 모아 배열에 추가
    for i, _ in dict:
        cnt = 0
        for x, y, z in idx:

            if i == y:
                if cnt == 2:
                    continue
                answer.append(x)
                cnt += 1
    return answer