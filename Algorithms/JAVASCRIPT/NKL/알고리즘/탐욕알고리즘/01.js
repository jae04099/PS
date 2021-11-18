// function solution(n) {
//   let coin = [500, 100, 50, 10, 5, 1];
//   let answer = 0;

//   n = 1000 - n;

//   for (let i = 0; i < coin.length; i++) {
//     while (n >= coin[i]) {
//       n -= coin[i];
//       answer++;
//     }
//   }

//   return answer;
// }

// console.log(solution(380));
// console.log(solution(1));


// function resultFunc(money) {
//   let nowMoney = 1000 - money;
//   let result = 0;
//   const coin = [500, 100, 50, 10, 5, 1];
//   for(let i = 0; i < coin.length ; i++){
//     while(nowMoney >= coin[i]){
//       nowMoney -= coin[i]
//       result++
//     }
//   }
//   return result
// }

// console.log(resultFunc(380))
// console.log(resultFunc(1))


let lists = [1, 2, 3, 4]

lists.sort((x, y) => y - x)

console.log(lists)