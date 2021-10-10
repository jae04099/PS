function solution(a, b) {
    var answer = 0;
    var c = 0
    if(a > b){
        c = a
        a = b
        b = c
    }
    for(let i = a ; i < b ; i++){
        answer += i
    }
    return answer;
}


console.log(solution(5, 3))