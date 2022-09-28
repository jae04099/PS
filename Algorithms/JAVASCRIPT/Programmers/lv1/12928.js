function solution(n) {
    var answer = 0;
    var tmpList = [];
    for (let i = 1; i <= n; i++) {
        if (n % i == 0) {
            tmpList.push(i)
        }
    }
    answer = tmpList.reduce((acc, val) => {
        return acc + val
    }, 0)
    return answer;
}