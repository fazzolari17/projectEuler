const smallestMultiple = () => {
  const multiples = []
  let count = 2
  for (let i = 1; i < 10; i++) {
    for(let j = count; j < 10000; j += count){
      multiples.push(j)

    }
    count++
  }
  console.log('END::', multiples.length-1)
  return multiples
}
const arr = smallestMultiple()

function getOccurrence(array, value) {
  return array.filter((v) => (v === value)).length;
}

const findNumber = (num) => {
  let numberOfOccurances = 0
  let count = 0
  while(numberOfOccurances < num) {
    if(numberOfOccurances === 10) {
      return `count: ${count} n: ${numberOfOccurances}`
    }
    numberOfOccurances = getOccurrence(arr, count)
    count++
  }
}
console.log(findNumber(10))
// console.log(getOccurrence(arr, 2520))