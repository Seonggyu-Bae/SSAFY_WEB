<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  
  <div class="navstyle">
    <nav>
      <RouterLink to="/">Home</RouterLink>  |
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </div>


  <RouterView />
</template>

<style scoped>
.navstyle{
  background-color: lightslategrey;
  text-align: center;
  padding-top: 10px;
  padding-bottom: 10px;
}

div > nav > a{
  text-decoration: none;
  color: white;
  margin: 0px 10px 0px 10px;
  
}
</style>
