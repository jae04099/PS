function solution(n) {
    var answer = 0;
    let tempStr = String(n);
    let tempArr = [];
    for (let i = 0; i < tempStr.length; i++) {
        tempArr.push(Number(tempStr[i]))
    }
    answer = tempArr.reduce((acc, val) => acc + val, 0)
    return answer;
}