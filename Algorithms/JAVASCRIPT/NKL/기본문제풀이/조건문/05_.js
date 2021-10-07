/*** 5. 네번째 좌표 ***/

/* user code */
function answer(x_arr, y_arr) {
  let result = [];
  let i = 0;
  x_arr.sort()
  y_arr.sort()
  // 코드 구현 시작 영역
    if(x_arr[i] == x_arr[i + 1] && i == 0){
      result.push(x_arr[2])
    }else{
      result.push(x_arr[0])
    }
    if(y_arr[i] == y_arr[i + 1] && i == 0){
      result.push(y_arr[2])
    }else{
      result.push(y_arr[0])
    }
  

  

  // 코드 구현 종료 영역

  return result;
}

/* main code */
let input = [
  // TC: 1
  [
    [5, 5, 8],
    [5, 8, 5],
  ],
  // TC: 2
  [
    [3, 1, 1],
    [2, 1, 2],
  ],
  // TC: 3
  [
    [7, 7, 3],
    [4, 1, 1],
  ],
];
for (let i = 0; i < input.length; i++) {
  process.stdout.write(`#${i + 1} `);
  console.log(answer(input[i][0], input[i][1]));
}
