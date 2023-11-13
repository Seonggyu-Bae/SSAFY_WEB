<template>
<RouterLink :to="{ name : 'main' }">main</RouterLink>
<h1>피니아와 라우터 연습하기</h1>
 
<RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>
