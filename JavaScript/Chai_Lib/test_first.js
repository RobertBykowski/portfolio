//console.log('Witaj świecie!');
// let fruits = ['apple', 'banana', 'orange'];
// console.log(fruits);

// let fruits = ['apple', 'banana', 'orange'];

// for (let i = 0; i < fruits.length; i++) {
//   console.log(fruits[i]);
// }

// let fruits = ['apple', 'banana', 'orange'];

// fruits.forEach(function(fruit) {
//   console.log(fruit);
// });

// const chai = require('chai');
// const expect = chai.expect;

// let fruits = ['apple', 'banana', 'orange'];

// fruits.forEach(function(fruit) {
//   console.log(fruit);
//   expect(fruit).to.be.oneOf(['apple', 'banana', 'orange']);
//   if (expect(fruit).to.be.oneOf(['appple', 'banana', 'orange'])) {
//     console.log('Asercja jest prawidłowa');
//   }
// });

// let x = 10;
// let y = 5;

// console.log('Dodawanie: ' + (x + y));
// console.log('Odejmowanie: ' + (x - y));
// console.log('Mnożenie: ' + (x * y));
// console.log('Dzielenie: ' + (x / y));


var answer = 43;

// AssertionError: expected 43 to equal 42.
expect(answer).to.equal(42);

// AssertionError: topic [answer]: expected 43 to equal 42.
expect(answer, 'topic [answer]').to.equal(42);



