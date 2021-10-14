/* 숫자 빈도수 구하기 */

/* user code */
function answer(s, e) {
  let result = [];
  let dics = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0};
  let sample = [];

  // 코드 구현 시작 영역

  for(let i = s; i <= e ; i++){
    let myFunc = num => Number(num)
    sample = Array.from(String(i), myFunc)
    for(let i = 0; i < sample.length ; i++){
      dics[sample[i]] += 1
      }
    }
    result = Object.values(dics)

  // 코드 구현 종료 영역

  return result;
}

/* main code */
let input = [
  // TC: 1
  [129, 137],

  // TC: 2
  [1412, 1918],

  // TC: 3
  [4159, 9182],
];

for (let i = 0; i < input.length; i++) {
  process.stdout.write(`#${i + 1} `);
  console.log(answer(input[i][0], input[i][1]));
}
