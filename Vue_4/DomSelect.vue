<template>
    <div>
        <input type="text" ref="input">
    </div>
</template>

<script setup>
import { ref } from 'vue'

// 직접 DOM 엘리먼트에 접근 해야 하는 경우 
//ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조를 얻을 수 있음
const input = ref()

console.log(input.value)
</script>

<style scoped>

</style>