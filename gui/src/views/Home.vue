<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld/>
    <Try/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Try from '@/components/Try.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Try
  }
}
</script>
