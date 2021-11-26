function solution(numbers) {
    const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    let answer = 0;
    for (let i = 0; i < list.length; i++) {
        if (!numbers.includes(list[i])) {
            answer += list[i]
        }
    }
    return answer;
}