<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage 
    v-for="info in store.balances"
    :key="info.name"
    :info="info"
    />
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '../components/MainPage.vue';
const store = useBalanceStore()
</script>

<style scoped>

</style>