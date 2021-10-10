function solution(price, money, count) {
    var answer = -1;
    let totalPrice = price
    for(let i = 2; i <= count ; i++){
        totalPrice += price * i
    }
    if(totalPrice > money){
        answer = totalPrice - money
    }else{
        answer = 0
    }
    return answer;
}

console.log(solution(3, 20, 4))