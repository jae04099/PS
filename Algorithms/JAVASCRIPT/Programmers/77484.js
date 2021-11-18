function solution(lottos, win_nums) {
    var answer = [];
    let zero = 0;
    zero = lottos.filter(e => 0 === e).length;
    let same = lottos.filter(e => win_nums.includes(e));
    if (zero === 6) {
        answer[1] = 6
    } else {
        answer[1] = 7 - same.length;
    }
    answer[0] = 7 - (same.length + zero)
    if (same.length + zero === 0) {
        return [6, 6]
    }
    return answer;
}