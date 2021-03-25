<template>
  <v-container fluid>
    <v-switch
      v-model="switch1"
      :label="`D1 Move: ${switch1.toString()}`"
    ></v-switch>
  </v-container>
  
</template>
<script>
  export default {
      name: "Try",
    
    data () {
      return {
        switch1: true,
      }
    },
  }
</script>