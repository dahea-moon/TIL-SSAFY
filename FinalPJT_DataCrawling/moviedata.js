const axios = require('axios');
const fs = require('fs');

axios.get('http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?collection=kmdb_new&detail=Y&listCount=300&releaseDts=20190101&releaseDte=20191124&ServiceKey=7J3BA5CHYBGW4H91UV78')
    .then(response => {
        let movieJson = [];
        let j = 1;
        res = response.data.Data[0].Result;
        res.forEach(movie => {
            let actors = "";
            for (let i=0; i < 3; i++) {
                try {
                    if (i < 2) {
                        actors += movie.actor[i].actorNm
                        actors += ","
                    } else {
                        actors += movie.actor[i].actorNm
                    }
                } catch(e) {}
            };
            let genre1 = movie.genre.split(',')[0]
            if (genre1 == '드라마') {
                genre1 = 1
            } else if (genre1 == '뮤직') {
                genre1 = 4
            } else if (genre1 == '아동') {
                genre1 = 7
            } else if (genre1 == '하이틴(고교)') {
                genre1 = 8
            } else if (genre1 == '청춘영화') {
                genre1 = 10
            } else if (genre1 == '무협') {
                genre1 = 23
            } else if (genre1 == '미스터리') {
                genre1 = 24
            } else if (genre1 == 'sf') {
                genre1 = 25
            } else if (genre1 == '코메디') {
                genre1 = 26
            } else if (genre1 == '액션') {
                genre1 = 28
            } else if (genre1 == '범죄') {
                genre1 = 29
            } else if (genre1 == '어드벤처') {
                genre1 = 30
            } else if (genre1 == '가족') {
                genre1 = 31
            } else if (genre1 == '에로') {
                genre1 = 32
            } else if (genre1 == '멜로드라마') {
                genre1 = 33
            } else if (genre1 == '공포') {
                genre1 = 34
            } else if (genre1 == '뮤지컬') {
                genre1 = 35
            } else if (genre1 == '스릴러') {
                genre1 = 38
            } else if (genre1 == '전쟁') {
                genre1 = 40
            } else if (genre1 == '판타지') {
                genre1 = 42
            }
            let genre2 = movie.genre.split(',')[1] != undefined ? movie.genre.split(',')[1] : null;
            if (genre2 == '드라마') {
                genre2 = 1
            } else if (genre2 == '뮤직') {
                genre2 = 4
            } else if (genre2 == '아동') {
                genre2 = 7
            } else if (genre2 == '하이틴(고교)') {
                genre2 = 8
            } else if (genre2 == '청춘영화') {
                genre2 = 10
            } else if (genre2 == '무협') {
                genre2 = 23
            } else if (genre2 == '미스터리') {
                genre2 = 24
            } else if (genre2 == 'SF') {
                genre2 = 25
            } else if (genre2 == '코메디') {
                genre2 = 26
            } else if (genre2 == '액션') {
                genre2 = 28
            } else if (genre2 == '범죄') {
                genre2 = 29
            } else if (genre2 == '어드벤처') {
                genre2 = 30
            } else if (genre2 == '가족') {
                genre2 = 31
            } else if (genre2 == '에로') {
                genre2 = 32
            } else if (genre2 == '멜로드라마') {
                genre2 = 33
            } else if (genre2 == '공포') {
                genre2 = 34
            } else if (genre2 == '뮤지컬') {
                genre2 = 35
            } else if (genre2 == '스릴러') {
                genre2 = 38
            } else if (genre2 == '전쟁') {
                genre2 = 40
            } else if (genre2 == '판타지') {
                genre2 = 42
            };
            let poster = movie.posters.split('|')[0]
            let ratingGrade = ""
            if (movie.rating[0].ratingGrade.indexOf('|') != -1) {
                ratingGrade += movie.rating[0].ratingGrade.split('||')[0]
            } else {
                ratingGrade += movie.rating[0].ratingGrade
            }
            let movie_made = { 
                title: movie.title,
                titleEng: movie.titleEng,
                director: movie.director[0].directorNm,
                actors,
                nation: movie.nation,
                plot: movie.plot,
                runtime: movie.runtime,
                genre1,
                genre2,
                ratingGrade,
                releaseDt: movie.repRlsDate,
                descriptions: movie.keywords,
                poster: poster,
                stills: movie.stlls,
                awards: movie.Awards1
            }
            let last = {
                pk: j++,
                model: 'movies.movie',
                fields: movie_made
            }
            movieJson.push(last)
        });
        movieJson = JSON.stringify(movieJson)
        fs.writeFile("moviedata.json", movieJson, 'utf8', function (err) {
            if (err) {
                return console.log(err)
            }
            console.log('success')
        })
    })


// fs.writeFile("moviedata.json", movieJson, 'utf8', function (err) {
//     if (err) {
//         return console.log(err)
//     }
//     console.log('success')
// })