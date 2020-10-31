const fs = require('fs')

const array = []
const regex = /[&\/\[\]#+()$~%'çÇ"´`^:„…*?–_ __ ___<>¨{}=|]/gim

const file = fs.readFile('file.txt', { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.log(err.message)
  } else {
    let newData = data.replace(regex, ' ').split(' ')
    newData.filter((e) => e != '')
    console.log('Quantity words:', newData.length)
    array.push(newData)
  }
})
