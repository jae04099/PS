/* 벽돌 옮기기 */

/* user code */
function answer(blocks) {
  let result = 0;
  let sum = 0;
  let aveNum = 0;
  let lists = []
  // 코드 구현 시작 영역

  for(let i = 0; i < blocks.length ; i++){
    sum += blocks[i]
  }

  aveNum = sum / blocks.length
  for(let i = 0; i < blocks.length; i++){
    if(parseFloat(blocks[i] - aveNum) > -1){
      lists.push(parseFloat(blocks[i] - aveNum))
    }
  }

  for(let i = 0 ; i < lists.length ; i++){
    result += lists[i]
  }

  // 코드 구현 종료 영역

  return result;
}

/* main code */
let input = [
  // TC: 1
  [5, 2, 4, 1, 7, 5],

  // TC: 2
  [12, 8, 10, 11, 9, 5, 8],

  // TC: 3
  [27, 14, 19, 11, 26, 25, 23, 15],
];

for (let i = 0; i < input.length; i++) {
  console.log(`#${i + 1} ${answer(input[i])}`);
}
