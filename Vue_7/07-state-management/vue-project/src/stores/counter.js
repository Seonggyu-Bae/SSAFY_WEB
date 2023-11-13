import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++, text: '할 일 1', isDone: false},
    { id: id++, text: '할 일 2', isDone: false},
  ])

  const addTodo = function(todoText){
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function(todoId){
    console.log('delete')
    // todo 배열에서 몇번째 인덱스가  삭제되었는지 검색
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // 찾은 인덱스 값을 통해 배열에서 요소를 제거 후 원본 배열 
    todos.value.splice(index, 1)
  }

  const updateTodo = function(todoId){
    console.log('update')
    todos.value = todos.value.map((todo) =>{
      if (todo.id === todoId){
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodosCount  = computed(() =>{
    return todos.value.filter((todo)=>todo.isDone).length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist : true })
