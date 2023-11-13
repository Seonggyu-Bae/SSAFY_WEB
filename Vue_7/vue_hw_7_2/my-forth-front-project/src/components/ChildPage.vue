<template>
  <div v-for="child of children" class="container">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  children : Object
})
</script>

<style scoped>

.container{
  background-color: white;
  margin: 10px 10px 20px 10px;
  border: 1px solid silver;
}

</style>