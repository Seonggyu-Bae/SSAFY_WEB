<template>
    <div class="container">

        <h2>가수 목록</h2>
        <SingerDetail imageUrl="@/src/assets/iu.jpg" />
        <SingerDetail imageUrl="@/src/assets/singer.jpg"/>
        <SingerDetail imageUrl="~@/src/assets/singer.jpg"/>
        <SingerDetail imageUrl="~@/src/assets/singer.jpg"/>

    </div>
    
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';


</script>

<style scoped>
h2{
    color: orangered;
}
.container {
    text-align: center;
}
</style>