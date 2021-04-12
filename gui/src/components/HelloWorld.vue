<template>
  <v-container>
  <p>{{mydata}}</p>
    <v-btn @click="func">Dej mi graf</v-btn>
  </v-container>
  
</template>
<script>
export default {
  name: "HelloWorld",

  data: () => ({
    mydata: {},
  }),

  methods: {
    func() {
      console.log("Jsem volana");

      window.eel.nacti_graf("Oven1Temperature1",100,"Timing")((result) => {
        this.mydata = result;
      });
    },
  },
};
</script>
