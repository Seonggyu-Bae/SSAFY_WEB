<template>
    <div>
        <ParentChild @some-event="someCallback"
        @emit-args="getNumbers" 
        my-msg="손틈새로 비치는 아이유 참 좋다" 
        :dynamic-props="name" />
    </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Winter')

const someCallback = function() {
    console.log('ParentChild가 발신한 이벤트 수신')
}

const getNumbers = function(...args){
    console.log(args)
    console.log(`ParentChilde가 전달한 추가인자 ${args} 수신 완료`)
}

</script>

<style  scoped>

</style>