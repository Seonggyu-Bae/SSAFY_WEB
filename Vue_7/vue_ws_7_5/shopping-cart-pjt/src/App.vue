<script setup>
import { RouterLink, RouterView } from 'vue-router'

import { useCounterStore } from './stores/products'
const store = useCounterStore()

</script>

<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>  
      <RouterLink :to="{name: 'products'}">Products</RouterLink>  
      <RouterLink :to="{name: 'favorite'}">Favorite
        <div v-if="store.howManyFavorites" class="round">
        {{ store.howManyFavorites }}
      </div></RouterLink>  
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

.round{
  border-radius: 10%;
  background-color: red;
  color: white;
  display: inline-block;
}
</style>
