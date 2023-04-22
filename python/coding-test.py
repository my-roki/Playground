def solution(keymap, targets):
    answer = []
    new_keymap = {}
    for k in keymap:
        for idx, word in enumerate(k):
            if new_keymap.get(word) == None:
                new_keymap[word] = idx + 1
            else:
                new_keymap[word] = min(new_keymap.get(word), idx + 1)

    for target in targets:
        result = 0
        is_fail = False
        for t in target:
            if new_keymap.get(t) == None:
                is_fail = True
                break
            result += new_keymap.get(t)

        if is_fail == False:
            answer.append(result)
        else:
            answer.append(-1)

    return answer


if __name__ == "__main__":
    print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))  # [9, 4]
    print(solution(["AA"], ["B"]))  # [-1]
    print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))  # [4, 6]
