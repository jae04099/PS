// function dfs(numbers, target, sums, index, total) {
//   if (index === numbers.length) {
//     return target === total ? 1 : 0;
//   }
//   if (
//     (target > total && target > total + sums[index]) ||
//     (target < total && target < total - sums[index])
//   )
//     return 0;

//   let count = 0;
//   count += dfs(numbers, target, sums, index + 1, total + numbers[index]);
//   count += dfs(numbers, target, sums, index + 1, total - numbers[index]);
//   return count;
// }

// function solution(numbers, target) {
//   let sums = new Array(numbers.length);
//   let sum = 0;

//   for (let i = numbers.length - 1; i >= 0; i--) {
//     sum += numbers[i];
//     sums[i] = sum;
//   }

//   return dfs(numbers, target, sums, 0, 0);
// }


// function solution(n, lost, reserve) {
//   let losted = [...lost].filter((x) => !reserve.includes(x));
//   let reserved = [...reserve].filter((x) => !lost.includes(x));
//   let answer = n - losted.length;

//   let db = {};
//   for (let i = 0; i < reserved.length; i++){
//     db[reserved[i]] = true;
//   }

//   losted = losted.sort((x, y) => x - y);
//   for (let i = 0; i < losted.length; i++){
//     if(db[losted[i] - 1]){
//       answer++
//       db[losted[i] - 1] = false;
//     }else if(db[losted[i] + 1]){
//       answer++;
//       db[losted[i] + 1] = false;
//     }
//   }
//   return answer;
// }

function solution(n, lost, reserve){
  // onlyLost와 onlyReserve는 서로 겹치는 사람이 없이 순수 배열을 만들어주기 위함이다.
  let onlyLost = [...lost].filter(x => !reserve.includes(x));
  let onlyReserve = [...reserve].filter(x => !lost.includes(x));

  // 이 둘이 정렬이 돼 있다는 확신이 없으므로 정렬도 시켜주자.
  onlyLost = onlyLost.sort((x, y) => x - y);
  onlyReserve = onlyReserve.sort((x, y) => x - y);

  // 우선 답은 전체 학생 수 에서 체육복이 없는 학생 수 일 것이다.
  let answer = n - onlyLost.length;

  // 이중 for문을 만들지 않기 위한 딕셔너리를 만들어주자.
  let isHaveCloth = {}; 

  // 그리고 확실하게 체육복을 가지고 있는 학생들의 key를 true로 만들어주자.active
  for(let i = 0 ; i < onlyReserve.length; i++){
    isHaveCloth[onlyReserve[i]] = true;
  }

  // 이제 체육복이 없는 학생들의 key를 돌면서 양 옆에 체육복을 빌려줄 수 있는 학생이 있나 살펴보자.
  for(let i = 0 ; i < onlyLost.length; i++){
    // 우선 이 전에 빌려줄 수 있는 학생이 있을까?
    if(isHaveCloth[onlyLost[i] - 1]){
      answer += 1;
      isHaveCloth[onlyLost[i] - 1] = false;
      // 이 후에 있다면
    }else if(isHaveCloth[onlyLost[i] + 1]){
      answer += 1;
      isHaveCloth[onlyLost[i] + 1] = false;
    }
  }
 return answer
}