<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>  
      <RouterLink :to="{name: 'products'}">Products</RouterLink>  
      <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>  
    </nav>
  </div>
  <RouterView />
</template>

<style scoped>
nav{
  text-align: center;
  background-color: dimgray;
  padding: 10px;

}
nav > a{
  margin-left: 20px;
  text-decoration: none;
  color: white;
}
</style>
