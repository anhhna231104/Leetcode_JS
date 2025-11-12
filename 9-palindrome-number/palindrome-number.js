/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {   
    if (x < 0){
        return false
    }
    
    let n = x, rev = 0
    while(n){
        let tmp = n % 10
        rev = rev * 10 + tmp
        n = parseInt(n / 10) 
    }

    return x == rev
};