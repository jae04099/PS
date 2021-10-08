/* 1. 등차수열의 항 찾기 */

/* user code */
function answer(a, d, n) {
  let index = -1;
  let i = 0;
  let lists = [];
  // 코드 구현 시작 영역

  while(a < n + 1){
    if(a == n){
      index = lists.length + 1
      break
    }
    a += d
    lists.push(a)
  }


  // 코드 구현 종료 영역

  return index;
}

/* main code */
let input = [
  // TC: 1
  [1, 2, 7],
  // TC: 2
  [2, 3, 10],
  // TC: 3
  [3, 5, 23],
];

for (let i = 0; i < input.length; i++) {
  console.log(`#${i + 1} ${answer(input[i][0], input[i][1], input[i][2])}`);
}
