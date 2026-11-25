const ArrayLetftRotator = (arr, d)=>{    
    while(d > 0){
        let shifted = arr.shift()        
        arr.push(shifted)
        d--
    }
    return arr
}

// console.log(ArrayLetftRotator([1,2,3,4,5], 3))


let holdingBox
let arr2 = [2,5,7,9,11]
let poppedElement = arr2.pop()
console.log(poppedElement)
holdingBox = arr2.shift()
// console.log(holdingBox)


// for(let i =0; i < arr.length;i++){
    // empty_pocket
    // go to machine
    // check for fakery
// }

/*
Write a function that finds the shortest string in a sentence.
eg: 
"Can we assume and declare the shortest string to be one"
*/

// const shortestDetector = (sentence)=>{    
//     let arr = sentence.split(" ")
//     let assumedShortest = arr[0]
//     let resArr = []
//     for(let i =0; i < arr.length; i++){
//         if (arr[i].length < assumedShortest.length){
//             resArr.push(arr[i])
//         }        
//     }
    
//     return resArr
// }

// console.log(shortestDetector("Can we assume and declare the shortest string to be one"))

const shortestDetector = (sentence)=>{    
    let arr = sentence.split(" ")
    let assumedShortest = arr[0]
    let resArr = []
        arr.forEach((el)=>{
            if (el.length < assumedShortest.length){
                resArr.push(el)
            }  
        })
              
    
    
    return resArr
}

// console.log(shortestDetector("Can we assume and declare the shortest string to be one"))



let arr1 = [3,5,5,3,4,2,2,3,5]
let val = 2

const removeElem = (arr, val)=>{
    for(let i = 0; i < arr.length; i++){
        if(arr[i] == val){
            arr.splice(i,1)            
            arr.push("_")
            i--
        }
        else{
            continue
        }
    }
    return arr
}

removeElem(arr1, val)

// let arr1 = [3,5,5,3,2,7,3,2,5]
// let val = 2
// for(key in obj){

// }

/*
Write a function that takes an array of integers [nums] 
and a target integer, return indices of the two numbers 
such that they add up to target. 

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.


nums = [2,4,5,8,9]
target = 11
*/


const elemSum = (arr, target)=>{
    let ans = []
    for(let i = 0; i < arr.length; i++){
        for(let j= i+1; j <arr.length; j++){
            if(arr[i] + arr[j] === target){
                ans.push(i,j)
            }
        }
    }
    return ans
}


// a function that sums all the elements of an array.
// a function that sum any number of inputs

const addThree = (a,b)=>{
    return a+b
}

const sumAnyInput = (a,b, ...rest)=>{
    let sum = a+b
    for(let i =0; i < rest.length; i++){
        sum+=rest[i]    
    }
    return sum
}

console.log(sumAnyInput(1,3,5,6,2,7,8))


let arr3 = [4,6,2,7,9]
