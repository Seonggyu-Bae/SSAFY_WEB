import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  const posts = ref([])

  const API_URL = 'http://127.0.0.1:8000'

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

  return { posts, API_URL, getPosts }
}, {persist: true })
