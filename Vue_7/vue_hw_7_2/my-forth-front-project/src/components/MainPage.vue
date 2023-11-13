<template>
  <div>
    <h1>pinia 연습하기</h1>
    <div>
      <ParentPage class="container"
      v-for="info in store.family"
      :key="info.familyName"
      :family="info" 
    />
    </div>

  </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue';
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

</script>

<style scoped>
.container{
  border: 1px solid silver;
  margin-bottom: 30px;
  margin-left: 100px;
  margin-right: 100px;
  text-align: center;
  background-color: whitesmoke;
}
</style>