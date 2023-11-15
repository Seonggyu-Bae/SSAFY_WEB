import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import PostListView from '@/views/PostListView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import CategoryCreateView from '@/views/CategoryCreateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainView
    },

    {
      path: '/posts',
      name: 'posts',
      component: PostListView
    },
    {
      path: '/post',
      name: 'post',
      component: PostCreateView
    },
    {
      path: '/category',
      name: 'categorycreate',
      component: CategoryCreateView
    },
    
  ]
})

export default router
