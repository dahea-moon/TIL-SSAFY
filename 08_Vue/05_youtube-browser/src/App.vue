<template>
<!-- HTML -->
    <div class="container">
        <!-- component는 재사용이 가능하기에 여러 개를 넣어서 쓸 수 있다 -->
        <SearchBar @inputChange="onInputChange"></SearchBar>
        <!-- v-on: [자식 comp에서 emit하는 이벤트 이름]="" -->

        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <VideoList 
                :videos="videos"
                @videoSelect="onVideoSelect"
            >
            </VideoList>
            <!-- 'v-bind:'는 줄여서 ':' -->
            <!-- props 쓰기: step0. bind 로 데이터를 넘긴다 -->
        </div>
    </div>
</template>

<script>
    import SearchBar from './components/SearchBar'; // 1. comp 불러오기
    import VideoList from './components/VideoList';
    import VideoDetail from './components/VideoDetail';
    import axios from 'axios';

    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

    export default {
        // 컴포넌트 만들면
        // 0. 이름적기
        name: 'App',
        components: {
            SearchBar, // 2. 자식인 components를 object 형태로 등록하기
            VideoList,
            VideoDetail,
        },
        data() {
            return {
                videos: [],
                selectedVideo: null,
            }
        },
        methods: {
            onInputChange (inputValue) {
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue,
                    }
                })
                .then(res => this.videos = res.data.items)
            },
            onVideoSelect (video) {
                this.selectedVideo = video;
            }
        },
    }
</script>

<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다 */
    input {
        width: 75%;
    }
    div {
        text-align: center;
        margin: 20px;
    }
</style>