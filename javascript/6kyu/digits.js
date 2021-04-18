// Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
// 
// we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
// In other words:
// 
// Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
// 
// If it is the case we will return k, if not return -1.



function digPow(n, p){
    // get number of digits in n
    const string = n.toString();
    const digits = string.length;
    
    // populate "list" with each digit in "n"
    let dividend = n;
    let list = [];
    for (let i = 0; i < digits; i++){
        list[i] = dividend % 10;
        dividend = Math.floor(dividend / 10);
    }
    list = list.reverse();
    let sum = 0;
    for (let i = 0; i < digits; i++){
        sum += Math.pow(list[i], i + p);
    }
    const divisor = sum / n;
    return (Number.isInteger(divisor) ? divisor : -1);
}
