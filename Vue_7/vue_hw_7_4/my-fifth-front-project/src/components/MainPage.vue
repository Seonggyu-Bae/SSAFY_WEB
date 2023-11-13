<template>
  <div>
    <p>이름: {{ info.name }}</p>
    <p>잔고: {{ info.balance }}</p>
    <RouterLink :to="{ name: 'update', params: {name:`${info.name}`} }"><button @click="">updateBalance</button></RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'

defineProps({
  info: Object
})

const store = useBalanceStore()



</script>

<style scoped>
button{
  background-color: dodgerblue;
  color: white;
}
</style>