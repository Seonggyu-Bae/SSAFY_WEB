<template>
    <div class="interval" v-for="child in dynamicProps" :key="child.name">
        <div class="box interval" >
            <h3>자식 페이지입니다.</h3>
            <p>이름 : {{ child.name }}</p>
            <p>나이 : {{ child.age }}</p>
        </div>
    </div>

</template>

<script setup>
defineProps({
    dynamicProps: Object,
})

// const children = defineProps({children: Object})
// console.log(children)
</script>

<style scoped>
.box{
  border: 1px silver solid
}
.interval{
    padding: 10px;
}


</style>