import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/icons/login.vue'
import RegisterUserView from './../components/RegisterUser.vue'
import DashboardView from './../components/icons/Dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
  ]
})

export default router
