function solution(n) {
    var answer = [];
    let tmpStr = String(n);
    for (let i = tmpStr.length - 1; i >= 0; i--) {
        answer.push(Number(tmpStr[i]))
    }
    return answer
}