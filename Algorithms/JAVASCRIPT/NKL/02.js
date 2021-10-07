let a = 12
let b = 10
let c = 0
let lists = []

if(a > b){
    c = a
    a = b
    b = c
}

for(let i = a ; i <= b ; i++ ){
    lists.push(i)
}

console.log(lists)