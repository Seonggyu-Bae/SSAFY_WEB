import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,

      // router.beforeEnter
      // route에 진입했을 때만 실행되는 함수
      // 매개변수, 쿼리 값이 변경될때는 실행되지 않고
      // 다른경로에서 탐색할 때만 실행됨
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      
      // 이미 로그인 상태라면 HomeView로 이동
      // 로그인 상태가 아니라면 LoginView로 이동하게 만들어보기
      beforeEnter: (to, from) =>{
        if(isAuthenticated === true){
          console.log('로그인 상태입니다.')
          return { name: 'home'}
        }
    },
    }
  ]})

// router.beforeEach((to, from) =>{
//   console.log(to)
//   console.log(from)

// })

// router.beforeEach((to, from)=>{
//   const isAuthenticated = false

//   if (!isAuthenticated && to.name!=='login'){
//     console.log('로그인이 필요합니다.')
//     return { name: 'login'}
//   }
// })


export default router
