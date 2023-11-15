<template>
  <div>
    <form @submit.prevent="createCategory">
      <div>
        <label for="name">Category 종류: </label><br>
        <input type="text" id="name" v-model.trim="category"><br>
        <input type="submit" value="카테고리 생성" class="btn btn-primary" >
      </div>

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const category = ref(null)

const createCategory = function(){
  store.createCategory(category)
}

</script>

<style scoped>
form{
  text-align: center;
}
</style>