import { createRouter, createWebHistory } from 'vue-router'
import AccountView from '../views/AccountView.vue'
import CarView from '../views/CarView.vue'
import MapView from '../views/MapView.vue'
import TireView from '../views/Car/TireView.vue'
import EngineView from '../views/Car/EngineView.vue'
import ACView from '../views/Car/ACView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'map',
      component: MapView
    },
    {
      path: '/car',
      name: 'car',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: CarView,
    },
    {
      path: '/account',
      name: 'account',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AccountView
    },
    {
      path: '/car/tires',
      name: 'tires',
      component: TireView,
    },
    {
      path: '/car/engine',
      name: 'engine',
      component: EngineView,
    },
    {
      path: '/car/ac',
      name: 'ac',
      component: ACView,
    },
  ]
})

export default router
