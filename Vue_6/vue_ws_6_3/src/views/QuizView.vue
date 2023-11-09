<template>
    <div>
        <QuizCreate @createQuiz="updateQuiz"/>
        <QuizDetail :quiz-list="quizList"/>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import QuizDetail from '../components/QuizDetail.vue';
import QuizCreate from '../components/QuizCreate.vue';

const quizList = ref([
    {pk:1, question:'Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?', answer:'flask'},
    {pk:2, question:'HTML에서 텍스트 입력란을 만드는데 사용되는 요소는?', answer:'input'},
    {pk:3, question:'웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?', answer:'post'},
    {pk:4, question:'Python의 가상환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?', answer:'virtualenv'},
    {pk:5, question:'웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?', answer:'html'},
])

const lstlen = computed(() => quizList.value.length)




const updateQuiz = function(...args) {
    event.preventDefault()
    // quizData를 이용하여 퀴즈를 업데이트하는 로직을 구현
    console.log(args[0].quiz)
    const newQuiz = {pk:lstlen.value+1, question:args[0].quiz, answer:args[0].answer}
    console.log(newQuiz)
    quizList.value.push(newQuiz)
    console.log(quizList.value)
}


</script>

<style scoped>

</style>