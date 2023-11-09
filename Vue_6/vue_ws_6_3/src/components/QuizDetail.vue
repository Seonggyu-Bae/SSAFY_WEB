<template>
    <div v-for="quiz in sortedQuizList" class="padtb" :id="quiz.answer">
        <div class="quizbox">
            <div class="pad">
                <p class="bold padt">{{`${quiz.pk}번 문제. ${quiz.question}`}} </p>
                <label :for="quiz.pk">정답 입력</label>
                <div class="padb">
                    <input type="text" :id="quiz.pk" style="width:600px; height: 30px;">
                </div>
            
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const { quizList } = defineProps(['quizList'])

const sortedQuizList = computed(() => [...quizList].sort((a, b) => b.pk - a.pk))
</script>

<style scoped>
.bold{
    font-weight: bold;
}

.quizbox{
    background-color: whitesmoke;
    border-radius: 10px;
    width: 100%;

}
.pad{
    padding-left: 10px;
}

.padtb{
    padding-top: 10px;
    padding-bottom: 10px;
}
.padt{
    padding-top: 10px;
}
.padb{
    padding-bottom: 10px;
}

input{
    border-radius: 5px;
}

</style>