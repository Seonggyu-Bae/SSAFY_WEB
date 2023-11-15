import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const router = useRouter()

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  

  const signUp = function(payload){
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    // const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username, password1, password2
      }
    })
      .then(res =>{
        const password = password1
        logIn({ username, password })
        console.log('회원가입 완료!')
      })
      .catch(err => console.log(err))
  }

  const token = ref(null)

  const logIn = function(payload){
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res =>{
        token.value = res.data.key
        console.log('로그인 완료')
        router.push({name: 'ArticleView' })
      })
      .catch(err => console.log(err))
  }

  // 토큰 여부에 따라 로그인 상태를 boolean 값으로 나타낼 isLogin 변수
  // computed를 활용해 token 값이 변할 때만 계산하도록 함
  const isLogin = computed(()=>{
    if (token.value === null) {
      return false
    }
    else{
      return true
    }
  })



  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
