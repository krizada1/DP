<template>
  <v-container>
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
      console.log("Jsem volanma");

      window.eel.load_data()((result) => {
        this.mydata = result;
      });
    },
  },
};
</script>
