const db = require('../src/connect/connect')
db.connect()

const XLSX = require('xlsx')
const data = XLSX.readFile('C:\Users\lang\Desktop\selenium\product.csv')

const jsonData = XLSX.utils.sheet_to_json(data);

console.log(jsonData)
