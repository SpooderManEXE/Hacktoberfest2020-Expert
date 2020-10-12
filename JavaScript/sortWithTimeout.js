
// Sorting an array of strings or numbers by using the setTimeOut function!

const arr = [1,5,3,7,100,2];
const arr2 = ['z','a','c'];

arr2.forEach((num)=>{
    if(typeof(num) === 'string')
    {
        setTimeout(()=>{
            console.log(num)
        },num.charCodeAt(0))
    }
    else
    {
        setTimeout(()=>{
            console.log(num)
        },num)

    }
})
