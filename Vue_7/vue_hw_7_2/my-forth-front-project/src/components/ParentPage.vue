<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage :children="family.children"/>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';
defineProps({
  family: Object,
})


</script>

<style scoped>

</style>