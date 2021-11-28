const numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
const left = [1, 4, 7];
const right = [3, 6, 9];
const mid = [2, 5, 8, 0];
const hand = 'right';
let answer = '';
let rightMove = 0;
let leftMove = 0;

let leftLocation = '*';
let rightLocation = '#';

for (let i = 0; i < numbers.length; i++) {
  if (left.includes(numbers[i])) {
    leftLocation = numbers[i];
    answer += 'L';
  } else if (right.includes(numbers[i])) {
    rightLocation = numbers[i];
    answer += 'R';
  } else {
    for (let j = 0; j < 3; j++) {
      if (numbers[i] - left[j] == 1) {
        leftMove++;
        break;
      } else {
        leftMove++;
      }
      if (right[j] - numbers[i] == 1) {
        rightMove++;
        break;
      } else {
        rightMove++;
      }
      if (rightMove > leftMove) {
        answer += 'R';
      } else if (rightMove < leftMove) {
        answer += 'L';
      } else {
        if (hand == 'right') {
          answer += 'R';
        } else {
          answer += 'L';
        }
      }
    }
  }
}

console.log(answer);