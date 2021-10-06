<template>
<n-config-provider :locale="zhCN" :date-locale="dateZhCN">
  <Setuppage />
</n-config-provider>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Setuppage from './components/Setuppage.vue'
import { NConfigProvider } from 'naive-ui'
import { zhCN, dateZhCN } from 'naive-ui'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Setuppage,
    NConfigProvider
  },
  setup() {
      return {
        zhCN,
        dateZhCN
      }
    }
}
</script>