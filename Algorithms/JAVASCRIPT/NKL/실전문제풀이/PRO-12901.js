function solution(a, b) {
    var answer = '';
    const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    const date = new Date(`${a} ${b} 2016`)
    answer = days[date.getDay()]
    return answer;
}

console.log(solution(5, 24))