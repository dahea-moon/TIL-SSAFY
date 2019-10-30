// es5
var colors = ['red', 'blue', 'green'];

for (var i=0; i < colors.length; i++) {
    console.log(colors[i])
}


// es6
// const colors = ['red', 'blue', 'green'];

function logger(x) {
    console.log(x)
}

colors.forEach(logger)

const numbers = [1, 2, 3];
const doubledNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i]*2)
}

console.log(doubledNumbers);

const test = numbers.map((number) => {
    return number * 3
});

console.log(test);

const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vege'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vege'},
];

const veges = products.filter((product) => {
    return product.type === 'vege'
});

console.log(veges);