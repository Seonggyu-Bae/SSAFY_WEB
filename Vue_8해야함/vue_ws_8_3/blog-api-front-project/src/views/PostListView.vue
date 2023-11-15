<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <ul>
      <li v-for="post in store.posts" :key="post.id">
        {{  post. title }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, computed, onMounted } from 'vue'
const store = useCounterStore()

onMounted(()=>{
  store.getPosts()
})


</script>

<style scoped>

</style>