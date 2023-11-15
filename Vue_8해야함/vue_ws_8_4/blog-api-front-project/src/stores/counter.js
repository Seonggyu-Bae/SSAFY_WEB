import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {

  const posts = ref([])
  const category = ref([])

  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const getCategory = function(){
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/`
    })
      .then(res => {
        category.value = res.data
        
      })
      .catch(err => console.log(err))
  }

  const getPosts = function(){
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/posts/`
    })
      .then(res => {
        posts.value = res.data
        console.log(res)
        console.log(res.data)
      })
      .catch(err => console.log(err))
  }

  const createCategory = function(name){
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/category/`,
      data: {
        name: name.value
      }
    })
      .then(res => {
        // router.push({name: 'home' })
      })
      .catch(err => console.log(err))
  }

  return { posts, category, API_URL, getPosts, createCategory, getCategory }
}, {persist: true })
