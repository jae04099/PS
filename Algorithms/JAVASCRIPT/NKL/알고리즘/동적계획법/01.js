// function solution(triangle) {
//   let answer = 0;
//   let height = triangle.length;
//   let d = Array(501)
//     .fill(0)
//     .map(() => Array(501).fill(0));
//   answer = d[0][0] = triangle[0][0];

//   for (let i = 1; i < height; i++) {
//     for (let j = 0; j <= i; j++) {
//       if (j == 0) d[i][j] = d[i - 1][j] + triangle[i][j];
//       else if (j == i) d[i][j] = d[i - 1][j - 1] + triangle[i][j];
//       else d[i][j] = Math.max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j];

//       answer = Math.max(answer, d[i][j]);
//     }
//   }

//   return answer;
// }

// const tc = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]];
// console.log(solution(tc));


// function solution(n, money){
//   let dp = new Array(n + 1).fill(0);
//   dp[0] = 1

//   for(let coin of money){
//     for(let price = coin; price <= n; price++){
//       dp[price] += dp[price - coin];
//     }
//   }
//   return dp[n] % 1000000007;
// }




// function solution(n, money){
//   let dp = new Array(n + 1).fill(0);
//   dp[0] = 1;
//   for(let coin of money){
//     for(let price = coin; price <= n; price++){
//       dp[price] += dp[price - coin];
//     }
//   }
// }

// let ascending_order = function(x, y){
//   if (typeof x == 'string') x = x.toUpperCase();
//   if (typeof y == 'string') y = y.toUpperCase();

//   return x > y ? 1 : -1;
// }
// let descending_order = function(x, y){
//   if (typeof x == 'string') x = x.toUpperCase();
//   if (typeof y == 'string') y = y.toUpperCase();

//   return x < y ? 1 : -1;
// }

// 피보나치
// 0, 1, 2, 3, 5
// dp[i] = dp[i - 1] + dp[i - 2]

// function fibo(n) {
//   if (n > 1) {
//     return fibo(n - 1) + fibo(n - 2)
//   } else {
//     return n
//   }
// }

// console.log(fibo(3))























