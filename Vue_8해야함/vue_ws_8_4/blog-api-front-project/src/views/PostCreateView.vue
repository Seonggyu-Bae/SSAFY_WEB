<template>
  <div>
    <h2 class="center">게시글 생성 페이지</h2>
    <div>
      <form class="center" @submit="createPost">
        <label class="center" for="category">카테고리 선택:</label><br>
        <select id="category" v-model="category">
          <option v-for="category in categorys">{{ category.name }}</option>
        </select>
        <br>

        <label for="title">제목:</label><br>
        <input class="center" type="text" id="title" v-model.trim="title"><br>
        <label for="content">내용:</label><br>
        <textarea class="center" id="content" v-model.trim="content" ></textarea>
        <br>
        <button type="button" class="btn btn-primary">게시글 생성</button>
      </form>
    </div>
    
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore()

const categorys = store.category

const category = ref(null)

const title = ref(null)
const content = ref(null)

const createPost = function(){
  store.createPost(category,title,content)
}


</script>

<style scoped>
.center{
  text-align: center;
}
</style>