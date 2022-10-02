function solution(s){
    let tmp = s.toLowerCase();
    let pCnt = 0;
    let yCnt = 0;
    for(i = 0 ; i < tmp.length ; i++){
        if(tmp[i] == 'p'){
            pCnt += 1;
        }else if(tmp[i] == 'y'){
            yCnt += 1;
        }
        if(i == tmp.length - 1){
            if(pCnt == yCnt){
                return true
            }else{{
                return false
            }}
        }
    }
}

console.log(solution('pPoooyY'))