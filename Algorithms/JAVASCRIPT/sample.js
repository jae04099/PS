const s = [1, 4, 8, 13, 14, 17, 20]
let res = 0
let temp = s[1] - s[0]

for(let i = 1; i < s.length ; i++){
    if(temp > (s[i] - s[i - 1])){
        temp = s[i] - s[i - 1]
        res = i
    }
}

console.log(s[res - 1], s[res])