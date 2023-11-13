import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
  ])

 
    const getUserByName = computed(()=>{
      return (name) => balances.value.find((obj)=>{
        return obj.name === name
      })
    })
  

  const giveThousand = function(name){
    balances.value = balances.value.map((who) =>{
      if( who.name === name ){
        who.balance += 1000
      }
      return who
    })
  }

  return { balances, giveThousand, getUserByName }
})
