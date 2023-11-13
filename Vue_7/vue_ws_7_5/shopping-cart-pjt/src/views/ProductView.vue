<template>
  <div class="container">
    <h1>상품 목록 페이지</h1>
    <div class="body">
      <ProductDetail class="card"
        v-for="item in store.productList"
        :key="item.name"
        :itemInfo="item"
      />
    </div>
  
  </div>
</template>

<script setup>
import ProductDetail from '../components/ProductDetail.vue';
import { useCounterStore } from '@/stores/products';


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