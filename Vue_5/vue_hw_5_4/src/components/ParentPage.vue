<template>
    <div class="box">
        <div>
            <h1>부모 페이지입니다.</h1>
        </div>
        <ChildPage @give-me-allowance="updateBalance" :dynamic-props="children" />
    </div>
</template>

<script setup>

import { ref } from 'vue'
import ChildPage from './ChildPage.vue';

const children = ref([
    {name: '김하나', age: 30, balance: 100000},
    {name: '김두리', age: 20, balance: 10000},
    {name: '김서이', age: 10, balance: 1000},
])

const updateBalance = function(child){
    child.balance += 1000
}

</script>

<style scoped>
.box{
  border: 1px silver solid
}
.interval{
    padding: 10px;
}
</style>