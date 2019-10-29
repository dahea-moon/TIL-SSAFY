const numbers = [1, 2, 3, 4];
// (4) [1, 2, 3, 4]
// 0: 1
// 1: 2
// 2: 3
// 3: 4
// length: 4
// __proto__: Array(0)


numbers[0];  // 1
numbers[-1]; // undefined. index는 양의 정수만 가능하다.
numbers.length; // 4

// 원본 파괴 method
numbers.reverse(); // (4) [4, 3, 2, 1]  <= return이 있음
numbers.reverse(); // (4) [1, 2, 3, 4]  <= return이 있고 원본도 바뀌고


numbers.push('a'); // 5 <= return 값(length)
numbers; // (5) [1, 2, 3, 4, "a"]


numbers.pop(); // 'a'
numbers; // (4) [1, 2, 3, 4]


numbers.unshift('a') // 5
numbers; // (5) ["a", 1, 2, 3, 4]
numbers.shift() // 'a'
numbers; // (4) [1, 2, 3, 4]


// 원본 그대로인 methods
numbers.includes(1) // true
numbers.includes('a') // false
numbers

numbers.indexOf(1); // 0

numbers.join() // "1,2,3,4"
numbers.join('') // "1234"
numbers.join('-')