<template>
  
    <div class="detail card">
        <h2>가수 이름</h2>
        <img class ="card-img-top" src="@/assets/singer.jpg" alt="singer" width="200">
        <p>가수 소개글</p>
    </div>

</template>

<script setup>
defineProps({
    imageUrl: String
})
</script>

<style scoped>

.detail{
    border: 1px solid black;
    text-align: center;
}
img{
    border-radius: 70%;
}

.card{
    display: inline-block;
    width: 40%;
    margin: 20px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
}

.container {
    text-align: center;
    
}


</style>