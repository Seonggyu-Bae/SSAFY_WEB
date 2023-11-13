<template>
  <div>
    <TodoListItem 
    v-for="todo in store.todos"
    :key="todo.id"
    :todoData="todo"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';
import TodoListItem from './TodoListItem.vue';

const store = useCounterStore()

</script>

<style scoped>

</style>