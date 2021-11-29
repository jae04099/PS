function solution(absolutes, signs) {
    for (let i = 0; i < absolutes.length; i++) {
        if (signs[i] == false) {
            absolutes[i] = -absolutes[i]
        }
    }

    let result = 0;
    result = absolutes.reduce((a, b) => a + b)
    return result
}