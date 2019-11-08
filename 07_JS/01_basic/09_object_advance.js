// ES5
// var => const/let

var books = ['Learning JS', 'Eloquent JS'];
var comics = {
    DC: ['Joker', 'batman'],
    marvel: ['avengers', 'spiderman'],
};
var magazine = {}

var bookshop = {
    books, comics, magazine
}
// key와 value 값이 같다면 그냥 위처럼 써도 된다
// key - value 에 같은 단어를 쓸때 축약할 수 있다


// method (객체 안의 함수)
// 절대 arrow function () => {} 쓰지말자
const me = {
    name: 'neo',
    // 메서드 정의
    greet: function () {
        return `Hello, ${this.name}`
    },
    // method: function 으로 정의하면 this가 const me이다
    // arrow function을 쓰면 this가 window가 된다
}
