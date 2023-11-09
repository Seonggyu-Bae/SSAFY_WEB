<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <div v-for="student in students">
      <nav>
        <p @click="goDetail(student.name)">{{ `${student.name} 학생 정보 보기` }}</p>
        <!-- <RouterLink :to="{ name : 'studentdetail',  }">Some</RouterLink> | -->
      </nav>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'

const students = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
])

const router = useRouter()
const studentName = ref('')
const goDetail = function(name){
  console.log(name)
  router.push({ name: 'studentdetail', params: {name:name} })
}

</script>

<style scoped>

</style>