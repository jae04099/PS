function solution(s) {
    const sDictionary = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
    var answer = 0;
    for (let i = 0; i < Object.keys(sDictionary).length; i++) {
        let letter = Object.keys(sDictionary)[i]

        // 아래의 방식으로 정규표현식 오브젝트 변수를 담아야 변수를 정규표현식에 사용할 수 있다.
        let regexAllCase = new RegExp(letter, "gi");
        if (s.includes(Object.keys(sDictionary)[i])) {
            s = s.replace(regexAllCase, Object.values(sDictionary)[i])
        }
    }
    answer = parseInt(s);
    return answer;
}