<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button type="button" class="btn btn-link" @click="goCreatePost">게시글 생성</button>
  
    <ul>
      <li v-for="post in store.posts" :key="post.id">
        {{ post. title }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()

onMounted(()=>{
  store.getPosts()
})

const goCreatePost = function(){
  router.push({name:'post'})
}


</script>

<style scoped>

</style>