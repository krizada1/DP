<template>
  <div class="home">
        <v-row>
            <v-col><Switches/></v-col>
            <v-col><Sliders/></v-col>
            <v-col></v-col>
            <v-col></v-col>
        </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import Switches from '@/components/Switches.vue'
import Sliders from '@/components/Sliders.vue'

export default {
  name: 'Home',
  components: {
    Switches,
    Sliders
  }
}
</script>
