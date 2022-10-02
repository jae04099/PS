function solution(n) {
    if (Math.sqrt(n) % 1 != 0) {
        return -1;
    } else {
        let tmp = Math.sqrt(n);
        return (tmp + 1) * (tmp + 1);
    }
}

console.log(solution(121))