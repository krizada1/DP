<template>
  <div class="home">
        <v-row>
            <v-col><Graphlist/></v-col>
            <v-col><HelloWorld/></v-col>
            <v-col></v-col>
            <v-col></v-col>
        </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Graphlist from '@/components/Graphlist.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Graphlist
  },
}
</script>
