<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3.0 + Vite" />
  <Naiveui />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Naiveui from './components/Naiveui.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Naiveui
  }
}
</script>