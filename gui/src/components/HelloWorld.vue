<template>
  <v-container>
  <p>{{mydata}}</p>
    <v-btn @click="func">Ahoj</v-btn>
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

      window.eel.nacti_z_db("D2Move", 1)((result) => {
        this.mydata = result;
      });
    },
  },
};
</script>
