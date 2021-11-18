// tree
// class Node{
//     constructor(data){
//         this.data = data;
//         this.children = [];
//     }

//     add(data){
//         this.children.push(new Node(data));
//     }

//     remove(data){
//         this.children = this.children.filter(child => child.data === data ? false : true)
//     }
// }

// class Tree{
//     constructor(){
//         this.root = null;
//     }
// }

// const t = new Tree();
// t.root = new Node('a');

// Array.prototype.sort
// 원본 배열을 직접 변경, 정렬된 배열을 반환
const fruits = ['Banana', 'Orange', 'Apple'];
// ascending
fruits.sort();
// descending
fruits.reverse();

// unicode 순서라서 문자열로 변환 후에 정렬해야 한다.
const points = [40, 100, 1, 5, 2, 25, 10];

// 반환 값이 0보다 작다는 것 은 a 가 b 보다 작다는거니까 그냥 그대로 둠. 그 반대라면 둘이 자리 바꿈.
points.sort(function(a, b){ return a - b });
points.sort((a, b) =>  a - b );

// descending
points.sort((a, b) => b - a);


// 만일 객체라면

const todos = [
    {id: 4, content: 'JS'},
    {id: 1, content: 'HTML'},
    {id: 2, content: 'CSS'}
]

function compare(key){
    return function(a, b){
        // 프로퍼티 값이 문자열이면 산술연산 - 로 비교할 때 NaN가 나옴. 때문에 비교연산자를 써야함.active

        return a[key] > b[key] ? 1 : (a[key] < b[key] ? -1 : 0)
    }
}

todos.sort(compare('id'));



// array.prototype.forEach
// for문 대신 사용 가능
// this를 변경하지 않음. 콜백함수는 가능.
// 가독성 좋음

const numbers = [1, 2, 3];
let pows = [];

numbers.forEach((item) => pows.push(item ** 2));

// array.prototype.map
// 새로운 배열 생성 반환

const numbers = [1, 4, 9];

const roots = numbers.map((item) => Math.sqrt(item));
// 두번째 인자에 this를 전달할 수 있는데 전달하지 않으면 this === window



// array.prototype.filter
// if문 대체
// True인 값만 추출한 새로운 배열 반환
const result = [1, 2, 3, 4, 5].filter((item, index, self) => {
    
})