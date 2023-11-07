<template>
    <div>
        <h2>MyComponent 요소 시작</h2>
        <MyComponentItem />
        <MyComponentItem />
        <MyComponentItem />
        <MyComponentItem />
        <p>MyComponentItem</p>
    </div>
</template>

<script setup>
import MyComponentItem from '@/components/MyComponentItem.vue';


</script>

<style scoped>
p {
    color: red
}

div{
    color: blue
}

</style>