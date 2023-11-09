<template>
    <div class="main">
        <div class="quizbox">
            <h3>퀴즈 생성</h3>
            <form @submit="create_quiz">
                <p>문제</p>
                <textarea class="mg" v-model="quiz" id="quiz" cols="100" rows="10"></textarea>
                <p>답안</p>
                <input class="" type="text" v-model="ans" id="ans" style="width:720px">
                <br>
                <input type="submit" value="퀴즈생성">
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['createQuiz'])
const quiz = ref('')
const ans = ref('')
const create_quiz = function(){
    emit('createQuiz',{quiz: quiz.value, answer: ans.value})
    quiz.value=''
    ans.value=''
}



</script>

<style scoped>
.main{
    text-align: center;
}
.quizbox{
    background-color: whitesmoke;
    border-radius: 10px;
    width: fit-content;
    
    margin: auto;

}
.pad{
    padding-left: 100px;
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
p,h3{
    text-align: left;
    padding-left: 10px;
}
.mg{
    margin: 10px;
}


</style>