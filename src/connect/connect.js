
const mongoose = require('mongoose');

async function connect() {
  try {
    await mongoose.connect('mongodb+srv://quelanh7412369:lanhpro101@cluster0.igg3ixr.mongodb.net/productdata?retryWrites=true&w=majority&appName=Cluster0');
    console.log('Kết Nối thành công');
  } catch (e) {
    console.error('Lỗi kết nối ', e);
  }
}
module.exports = { connect };