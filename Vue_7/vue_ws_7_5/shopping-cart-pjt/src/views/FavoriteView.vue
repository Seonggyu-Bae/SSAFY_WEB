<template>
  <div>
    <h1>장바구니 페이지</h1>
    <div class="body">
      <ProductDetail class="card"
        v-for="item in store.favoriteProducts"
        :key="item.name"
        :itemInfo="item"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/products';
import ProductDetail from '../components/ProductDetail.vue';
const store = useCounterStore()


</script>

<style scoped>
.body{
  text-align: center;
}
.card{
  border: 2px solid gainsboro;
  display: inline-block;

}
</style>