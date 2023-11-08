<template>
    <div v-for="child in dynamicProps" :key="child.name">
        <div class="box interval">
            <h3>자식 페이지입니다.</h3>
            <p>이름 : {{ child.name }}</p>
            <p>나이 : {{ child.age }}</p>
            <p>용돈 : {{ child.balance }}</p>
            <button @click="emitData(child)">용돈 주세요.</button>
        </div>
    </div>

</template>

<script setup>
defineProps({
    dynamicProps: Object,
})

const emit = defineEmits(['giveMeAllowance', 'emitData'])
const emitData = function(child){
    
    emit('giveMeAllowance',child)
}

</script>

<style scoped>
.box{
  border: 1px silver solid
}
.interval{
    padding: 10px;
    margin-top: 10px;
}


</style>