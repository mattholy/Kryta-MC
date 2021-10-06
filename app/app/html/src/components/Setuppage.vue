<template>
<div class="steps">
<n-steps :current="current" :status="currentStatus">
      <n-step
        title="欢迎使用Kryta"
        description="接下来我们将会开始进行一系列设置"
      />
      <n-step
        title="注册管理员账号"
        description="这里，你需要注册一个管理员账号来管理Kryta"
      />
      <n-step
        title="Come Together"
        description="Here come old flat top He come grooving up slowly"
      />
      <n-step
        title="Something"
        description="Something in the way she moves Attracts me like no other lover"
      />
    </n-steps>
</div>

<div class="main-container">
  <n-card
    title="欢迎使用Kryta"
    :segmented="{
      content: 'hard',
      footer: 'soft'
    }"
  >
    <n-form>
          <n-form-item-row label="用户名">
            <n-input />
          </n-form-item-row>
          <n-form-item-row label="密码">
            <n-input />
          </n-form-item-row>
          <n-form-item-row label="重复密码">
            <n-input />
          </n-form-item-row>
          <n-button type="primary" @click="next">下一步</n-button>
        </n-form>
    <template #action> #action </template>
  </n-card>
</div>
</template>

<style>
.main-container {
  width: 50%;
  margin: auto;
}
.steps {
  padding: 20px;
}
</style>

<script>
import { defineComponent, ref } from 'vue'
import { MdArrowRoundBack, MdArrowRoundForward } from '@vicons/ionicons4'

export default defineComponent({
  components: {
    MdArrowRoundBack,
    MdArrowRoundForward
  },
  setup () {
    const currentRef = ref(1)
    return {
      currentStatus: ref('process'),
      current: currentRef,
      next () {
        if (currentRef.value === null) currentRef.value = 1
        else if (currentRef.value >= 4) currentRef.value = null
        else currentRef.value++
      },
      prev () {
        if (currentRef.value === 0) currentRef.value = null
        else if (currentRef.value === null) currentRef.value = 4
        else currentRef.value--
      }
    }
  }
})
</script>