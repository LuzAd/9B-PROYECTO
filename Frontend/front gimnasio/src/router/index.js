import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/icons/login.vue'
import RegisterUserView from '@/components/icons/RegisterUser.vue'
import DashboardView from './../components/icons/Dashboard.vue'
import Home from '@/components/icons/Home.vue'
import Persona from '@/components/icons/Persona.vue'

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
      component: DashboardView,
      children:[
        {path:'/home', name: 'home', component:Home},
        {path:'/personas', name: 'personas', component: Persona}
      ]
    },
  ]
})

export default router
