/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let s_formatted = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let s_rev = s_formatted.split('').reverse().join('');
    return s_rev === s_formatted
};