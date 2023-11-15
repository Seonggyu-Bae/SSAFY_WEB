<template>
  <div class="box">
    <h1>블로그 메인 페이지</h1>
    <p>갈 길이 멀구만</p>
    <br>
    <br>
    <h3>카테고리 목록</h3>
    <div v-for="category in categorys" :key="category.id"  class="category">
      <p>{{ category.name }}</p>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from "@/stores/counter"

const store = useCounterStore()
onMounted(()=>{
  store.getCategory()
})
const categorys = ref(store.category)

</script>

<style scoped>
.box{
  text-align: center;
  background-color: silver;
}
.category{
  background-color: white;
  display: inline-block;
  margin: 10px 10px 10px 0px;
  padding-left: 20px;
  padding-right: 20px;
  border-radius: 7%;
}
</style>