// var _ = require('lodash');
// let list = ['a','b','c']

// let pick = _.sample(list)
// let num = _.range(1,46)
// let lottery = _.sampleSize(num, 6)

// let menu = {
//     a:'https://image.flaticon.com/icons/svg/511/511121.svg',
//     b:'https://image.flaticon.com/icons/svg/511/511122.svg',
//     c:'https://image.flaticon.com/icons/svg/511/511123.svg',



// }

// console.log(`알파벳 ${pick}`)
// console.log(menu[pick])

// console.log(`행운의 번호 6개: ${lottery}`)


// let getMin = (a,b) => {
//     if (a>b){
//         return b
//     }
//     return a
// }


// let getMinFromArray = nums =>{
//     let min = Infinity
//     for (num of nums){
//         if (min>num){
//             min = num
//         }
//     }
//     return min
// }


// ssafy = [0,2,3,4,5,]
// console.log(getMinFromArray(ssafy))

// const myObject ={
//     key:'Value'
// }

// console.log(myObject.key)
// console.log(myObject['key'])

let concat = (str1,str2) => {
    return `${str1} - ${str2}`
}
let check_long_str = (string) => {
    if(string.length>10){
        return true
    } 
    return false
}

if (check_long_str(concat('Happy', 'Hecking'))){
    console.log('LONG STRING')
}else{
    console.log('SHORT STRING')
}

