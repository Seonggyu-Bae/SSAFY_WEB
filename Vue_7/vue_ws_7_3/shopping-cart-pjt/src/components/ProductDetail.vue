<template>
  <div>
    <p class="name">{{ itemInfo.name }}</p>
    <img :src="`${itemInfo.imagePath}`" alt="">
    <p>\ {{ itemInfo.price }}</p>

    <span @click="store.updateFavorite(itemInfo.name)">
      <i v-if="itemInfo.isFavorite" class="fa-solid fa-heart"></i>
      <i v-else class="fa-regular fa-heart"></i>
    </span>
 
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/products';

defineProps({
  itemInfo: Object,
})

const store = useCounterStore()


</script>

<style scoped>
img{
  width: 250px;
  height: 150px;
}
.name{
  font-weight: bold;
}
div{
  margin-left: 20px;
  margin-bottom: 10px;
}
div > img{
  margin-left: 10px;
  margin-right: 10px;
}
i{
  margin-bottom: 40px;
}
</style>