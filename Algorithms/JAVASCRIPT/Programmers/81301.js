function solution(s) {
    const sDictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    var answer = 0;
    for(let i = 0; i < Object.keys(sDictionary).length ; i++){
    let letter = Object.keys(sDictionary)[i]
    let regexAllCase = new RegExp(letter, "gi");
    if(s.includes(Object.keys(sDictionary)[i])){
        s = s.replace(regexAllCase,Object.values(sDictionary)[i])
    }
}
answer = parseInt(s);
    return answer;
}