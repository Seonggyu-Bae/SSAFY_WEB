<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름: {{ store.getUserByName(userName).name }}</p>
    <p>잔고: {{ store.getUserByName(userName).balance }}</p>
    <button @click="store.giveThousand(userName)">+</button>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const userName = ref(route.params.name)
const store = useBalanceStore()


// const info = store.returnObject(userName)


</script>

<style scoped>

</style>