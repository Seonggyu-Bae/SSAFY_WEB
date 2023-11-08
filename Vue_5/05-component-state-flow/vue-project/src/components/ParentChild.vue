<template>
    <div>
        <p>{{ myMsg }}</p>
        <!-- 한 단계 더 prop 내려 보내기 -->
        <!-- ParentChild 컴포넌트에서 Parent로 부터 받은 prop인 myMsg를 ParentGrandChild에게 전달 -->
        <!-- v-bind를 사용한 동적 props -->
        <ParentGrandChild :my-msg="myMsg"/>

        <!-- Dynamic props -->
        <p>{{ dynamicProps }}</p>

        <button @click="$emit('someEvent')">클릭 이벤트 보내기</button>

        <button @click="buttonClick">이벤트 선언 방식</button>

        <button @click="emitArgs">추가 인자 전달</button>

    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 문자열 배열을 사용한 Props 선언
// defineProps(['myMsg'])

// 객체를 사용한 props 선언 (권장)
defineProps({
    myMsg: String,
    dynamicProps: String,
})

// props를 객체로 반환하므로 필요한 경우 JS에서 접근 가능
// const props = defineProps({ myMsg: String})
// console.log(props)
// console.log(props.myMsg)

// 이벤트 선언 방식으로 작성 (defineEmits())
const emit = defineEmits(['someEvent', 'emitArgs'])

const buttonClick = function(){
    emit('someEvent')
}

const emitArgs = function(){
    emit('emitArgs', 1, 2, 3)
}

</script>

<style  scoped>

</style>