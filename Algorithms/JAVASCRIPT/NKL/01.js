const star = '*';
let lists = []
const num = [5, 7, 12]
for(let i = 0 ; i < num.length ; i++){
    for(let j = 0 ; j < num[i] ; j++){
        lists.push(star)
    }
    console.log(lists.join(''))
    lists = []
}