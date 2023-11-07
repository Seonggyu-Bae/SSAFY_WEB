<template>
    <div>
        <input type="text" v-model="colorClass">
        <p :class="{red:colorClass==='red',green:colorClass==='green', blue:colorClass==='blue' }">입력창에 올바른  색상 명을 입력하면 글자색이 바뀝니다.</p>
        <p :style="{color:colorClass}">입력창에 올바른 색상 명을 입력하면 글자색이 바뀝니다.</p>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    const colorClass = ref('')
</script>


<style scoped>
.red{
    color: red;
}

.blue{
    color: blue;
}

.green{
    color: green;
}
</style>