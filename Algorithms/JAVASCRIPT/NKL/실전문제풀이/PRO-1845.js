function solution(nums) {
    var answer = 0;
    let setList = new Set(nums)
    let numForChoice = nums.length / 2
    if(setList.size < numForChoice){
        answer = setList.size
    }else {
        answer = numForChoice
    }
    return answer;
}

console.log(solution([3, 3, 3, 2, 2, 2]))