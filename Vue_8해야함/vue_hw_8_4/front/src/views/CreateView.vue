<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="">제목 : </label>
      <input type="text" id="title" v-model.trim="title">
      <label for="">내용 : </label>
      <textarea id="content" v-model.trim="content"></textarea>

      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref } from 'vue'
import router from '../router';
import axios from 'axios'

const store = useArticleStore()
const title = ref(null)
const content = ref(null)

const createArticle = function(){
  store.createArticle(title.value,content.value)
}



</script>

<style scoped>

</style>