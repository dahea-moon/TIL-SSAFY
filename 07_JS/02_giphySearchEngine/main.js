// 1. input 태그 안의 값(value)를 잡는다.
// const input = document.querySelector('#js-userinput').value;

// 2-1. button 태그에는 'click'이 일어났을 때, input에 ENTER키를 쳤을 때, Event listener를 단다.
// [무엇].addEventListener([언제], [어떻게])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const inputCount = document.querySelector('#js-image-count');
const resultArea = document.querySelector('#js-result-area');

// const API_KEY = '18m2PwhbQE0bWzfk074djIi0ncgodhwm';
// const test_word = 'dog'
// const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}}&q=${test_word}&limit=5&offset=0&rating=G&lang=ko`;
// console.log(url);

// const whenClicked = function () {
//     console.log('클릭!')
// }

// const whenPressed = function (event) {
//     console.log('꾸욱');
//     console.log(event);
// }

button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    // const inputCountValue = inputCount.value;
    searchAndPush(inputValue);
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value;
        // const inputCountValue = inputCount.value;
        // 2-2. 1에서 잡은 값을 Giphy API 에 요청 보내서 받기
        searchAndPush(inputValue);
    }
});

// 3. Giphy API 에서 넘겨준 Data를 index.html에서 보여준다.
const searchAndPush = (keyword) => {
    const API_KEY = '18m2PwhbQE0bWzfk074djIi0ncgodhwm';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=10&offset=0&rating=G&lang=ko`;
    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url); // 요청 세팅
    AJAX.send(); // 요청 보내기

    resultArea.innerHTML = null;
    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;

        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        };
    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-img';
        imageTag.classList.add('container-image')
        resultArea.appendChild(imageTag);
        // resultArea.innerHTML += `<img src="${imgUrl}" class="container-image">`;
    };
};

// const sendAjaxReq = () => {
//     const AJAX = new XMLHttpRequest(); // 요청 준비
//     AJAX.open('GET', url); // 요청 세팅
//     AJAX.send(); // 요청 보내기

//     AJAX.addEventListener('load', (answer) => {
//         const res = answer.target.response;
//         const giphyData = JSON.parse(res);
//         console.log(giphyData);
//     });
// }