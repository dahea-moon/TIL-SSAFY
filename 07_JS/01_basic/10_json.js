// JavaScript Object Notation: JS의 Object처럼 표기하는 방법
// JSON으로 표현된 데이터의 타입은 무조건 string

const rawJSON = '{ "name": "moon","job": "teacher"}';

// parsing: 구문분석
const parsedData = JSON.parse(rawJSON);
// serializing: 공용어로 번역(직렬화)
const backToJson = JSON.stringify(parsedData);
