const fs = require('fs')
const path = require('path')

const names = fs.readFileSync(path.resolve(__dirname, 'problem22_names.txt'), 'utf8')

const converFileToArray = (file) => {

  let tempArr = []
  let arr = file.split(',')
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== ',') {
      tempArr.push(arr[i])
    }

  }
  return tempArr.sort()
}

const alphabetHashMap = () => {
  let alph = '"abcdefghijklmnopqrstuvwxyz'
  alph = alph.toUpperCase()
  alph = alph.split('')
  const alphabetMap = new Map()

  alph.forEach((e, i) => {
    alphabetMap.set(e, i)
  })
  return alphabetMap
}

const pp = (item) => {
  console.log(item)
}


const longestName = (names) => {
  const hashMap = alphabetHashMap()
  let runningTotal = 0

  for (let i = 0; i < names.length; i++) {
    let count = 0
    for (let j = 0; j < names[i].length; j++) {
      let current = hashMap.get(names[i][j])
      count = count + current
    }
    count = count * (i+1)
    runningTotal = runningTotal + count
  }
  return runningTotal
}



pp(longestName(converFileToArray(names)))
const test1 = ['THIS', 'IS', 'ONLY', 'A', 'TEST']
const test2 = ['I', 'REPEAT', 'THIS', 'IS', 'ONLY', 'A', 'TEST']
pp(longestName(test1))
pp(longestName(test2))

pp(converFileToArray(names))
