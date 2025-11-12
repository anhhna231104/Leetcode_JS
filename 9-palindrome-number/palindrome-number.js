/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {   
    if (x < 0){
        return false
    }
    
    let x_formatted = String(x).split('').reverse().join('')
    
    return x == parseInt(x_formatted)
};