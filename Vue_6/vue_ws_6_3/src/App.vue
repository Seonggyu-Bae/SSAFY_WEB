<template>
  <div class="w">

    <div class="box padd rad">

      <div class="radi padd">
        <div class="orange pdtb">
          <h3>Quiz 퀴즈</h3>
        </div>
        <div class="white pdtb">
          <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요.
            지금 바로 도전해보세요!
          </p>
        </div>
      </div>

      <div class="q">
        <nav class="nav">
          <RouterLink class="nav" :to="{ name: 'home' }">Home</RouterLink>      |
          <RouterLink class="nav" :to="{ name: 'quiz' }">Quiz</RouterLink>      |
        </nav>
      </div>
    </div>

  </div>

  <RouterView />
</template>

<script setuo>
import { RouterLink, RouterView } from 'vue-router';
</script>
<style  scoped>
  .w{
    width: fit-content;
    text-align: center;
    margin:auto; 
    
  }
  .box{
    background-color: silver;
    text-align: center;
  }
  .padd{
    padding: 10px;
    padding-top: 10px;
  }
  .pdtb{
    padding-top: 10px;
    padding-bottom: 10px;
  }
  .q{
    text-align: center;
    padding: 10px;
    padding-top: 10px;
    background-color: black;
    
  }
  .nav{
    text-decoration: none;
    color: white;
  }
  .orange{
    background-color: orange;
    color: white;
  }
  .white{
    background-color: white;
  }

  .radi{
    border-radius: 5%;
  }
</style>
