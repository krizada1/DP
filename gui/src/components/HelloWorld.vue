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

      window.eel.load_data(57)((result) => {
        this.mydata = result;
      });
    },
  },
};
</script>
