// const board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]];
// const moves = [1, 5, 3, 5, 1, 2, 1, 4]
// const result = 4;

// let basket = [];

// for (let i = 0; i < moves.length; i++) {
//         for (let k = 0; k < 5; k++) {
//             if(board[moves[i] - 1][k] !== 0){
//                 basket.push(moves[i])
//                 board[moves[i] - 1][k] = 0
//                 break
//             }
//         }
//     }

// console.log(basket)


// https://velog.io/@qmasem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%AC%EB%A0%88%EC%9D%B8-%EC%9D%B8%ED%98%95%EB%BD%91%EA%B8%B0-%EA%B2%8C%EC%9E%84-JavaScript

function solution(board, moves) {
    const basket = [];
    let result = 0;
    moves.forEach(order => {
        const doll = pickup(board, order-1);
        if(doll){
            if(basket[basket.length-1] === doll){
                basket.pop();
                result +=2;
            }else{
                basket.push(doll);
            }
        }
    });
    return result;
}

function pickup(board, order){
    for(let i = 0; i < board.length ; i++){
        if(board[i][order] !== 0){
            const doll = board[i][order];
            board[i][order]= 0;
            return doll;
        }
    }
}