const start = Date.now()

const smallestMultiple = (n, m )=> {
 let i = n

  for(let i = n; i < 1000000000;  i+=n){
    for(let j = m; m > 0; m-- ){ 
      if (i % j !== 0)
    }

  }
}
// let i = 20
// while( i % 2 !== 0 ||  i % 3 !== 0 ||  i % 4 !== 0 ||  i % 5 !== 0 || i % 6 !== 0
//   ||  i % 7 !== 0 ||  i % 8 !== 0  || i % 9 !== 0 ||  i % 10 !== 0 || i % 11 !== 0
//   ||  i % 12 !== 0 ||  i % 13 !== 0 ||  i % 14 !== 0 || i % 15 !== 0 ||  i % 16 !== 0 
//   ||  i % 17 !== 0  || i % 18 !== 0 ||  i % 19 !== 0 || i % 20 !== 0)
// {
//   i+=20
// }

console.log(i)
const end = Date.now()
console.log(`${end - start}MS`)
