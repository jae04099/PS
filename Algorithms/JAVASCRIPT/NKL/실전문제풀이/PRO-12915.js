function solution(strings, n) {
    var answer = [];
    // strings.sort(function(a, b){
    //     var first = a[n]
    //     var second = b[n]
    //     if(first == second){
    //         return (a > b) - (a < b);
    //     }else {
    //         return (first > second) - (first < second)
    //     }
    // })
    return strings.sort((x, y) => x[n] == y[n] ? (x > y ? 1 : -1) : (x[n] > y[n] ? 1 : -1));
}

console.log(solution(["sun", "bed", "car"], 1))