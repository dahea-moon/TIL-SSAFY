// KEY-VALUE json
// Javascript Object Notation: JS의 Object처럼 표기하는 방법

const me = { // Object - 객체
    name: 'dahea', // key string 한 단어 일때는 따옴표 생략 가능
    'phone number': '01027421194', // key가 여러 단어일때는 써야함
    electronicDevice: {
        phone: 'galaxy 8',
        labtop: 'samsung 9',
    } ,
}

me.electronicDevice.phone
me['electronicDevice']['phone']

