let result = []

function filter(arr, i, j, k) {
    if (i == j) {
        return arr[i - 1]
    }
    // splice는 원본 배열을 변경한다.
    let temp = arr.slice(i - 1, j).sort((a, b) => a - b)[k - 1]
    return temp
}


function solution(array, commands) {
    for (let i = 0; i < commands.length; i++) {
        let arr = [...array]
        result.push(filter(arr, commands[i][0], commands[i][1], commands[i][2]))
    }
    return result
}