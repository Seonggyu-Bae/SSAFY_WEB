import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles`
    })
    .then(res => {
      console.log(res)
      articles.value = res.data
    })
    .catch(err=> console.log(err))

  }

  const createArticle = function(title,content){
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data:{
        title: title,
        content: content,
      }
  
    })
      .then(() =>{
        router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
    
  }



  return { articles, API_URL, getArticles, createArticle }
}, {persist: true })
