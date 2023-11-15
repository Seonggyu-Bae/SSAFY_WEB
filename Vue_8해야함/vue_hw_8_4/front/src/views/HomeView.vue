<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button @click="createArticle">게시글 생성</button>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '../components/ArticleList.vue';
import { useArticleStore } from '@/stores/articles'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const router = useRouter()

const createArticle = function(){
  router.push({ name: 'create' })
}



</script>

<style lang="scss" scoped>

</style>