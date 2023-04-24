import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import user_data from '../data/user_data.csv'

export const useUserStore = defineStore('users', () => {

  const all_users = ref(user_data)

  return { all_users } 
})
