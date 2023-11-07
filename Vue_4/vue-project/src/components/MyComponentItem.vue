<template>
    <div>
        <p>MyComponent의 아이템으로 사용할 예정입니다.</p>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>

<!-- <template>
    <div>
        <input type="text" ref="input">
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 직접 DOM 엘리먼트에 접근 해야 하는 경우 
//ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조를 얻을 수 있음
const input = ref()
onMounted(()=>{
    console.log(input.value)
})

</script>

<style scoped>

</style> -->