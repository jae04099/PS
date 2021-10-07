/*** 5. 무한 뺄셈 ***/

/* user code */
function answer(s, e) {
  let sequence = [];
  let i = 3;
  sequence.push(s);
  sequence.push(e);

  // 코드 구현 시작 영역

  while(1){
    i = s - e;
    s = e
    e = i
    if(i < 0) break;
  
  sequence.push(i)
  }

  // 코드 구현 종료 영역

  return sequence;
}

/* main code */
let input = [
  // TC: 1
  [9, 3],
  // TC: 2
  [6, 3],
  // TC: 3
  [13, 7],
];

for (let i = 0; i < input.length; i++) {
  process.stdout.write(`#${i + 1} `);
  console.log(answer(input[i][0], input[i][1]));
}
