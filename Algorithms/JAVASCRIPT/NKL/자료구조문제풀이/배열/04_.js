/* 일곱 난장이 */

/* user code */
function answer(dwarf) {;
  let fakers = [];
  let sum = 0;
  // 코드 구현 시작 영역
  for(let i = 0 ; i < dwarf.length ; i++){
    sum += dwarf[i]
  }

  let faker = sum - 100;

  for(let i = 0; i < dwarf.length ; i++){
    for(let j = i + 1; j < dwarf.length ; j++){
      if(dwarf[i] + dwarf[j] == faker){
        fakers.push(dwarf[i])
        fakers.push(dwarf[j])
        break
      }
    }
    if(fakers.length != 0){
      break
    }
  }

  let count = 0;
  for(let i = 0 ; i < dwarf.length ; i++){
    if(dwarf[i] != fakers[0] && dwarf[i] != fakers[1]){
      dwarf[count++] = dwarf[i]
    }
  }
  result = dwarf
  

  // 코드 구현 종료 영역

  return result;
}

/* main code */
let input = [
  // TC: 1
  [1, 5, 6, 7, 10, 12, 19, 29, 33],

  // TC: 2
  [25, 23, 11, 2, 18, 3, 28, 6, 37],

  // TC: 3
  [3, 37, 5, 36, 6, 22, 19, 2, 28],
];

for (let i = 0; i < input.length; i++) {
  process.stdout.write(`#${i + 1} `);
  console.log(answer(input[i]));
}
