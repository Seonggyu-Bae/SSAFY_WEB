<template>
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit" value="">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue'

const todoText = ref('')

const store = useCounterStore()
const formElem = ref(null)


const createTodo = function(todoText){
  store.addTodo(todoText)
  formElem.value.reset()
}



</script>

<style scoped>

</style>