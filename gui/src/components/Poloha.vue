<template>
  <div class="text-center">
    <v-row justify="center"> X: {{ value_X }} </v-row>
    <br />
    <v-row justify="center"> Y: {{ value_Y }} </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value_X: "nedefinovano",
      value_Y: "nedefinovano",
    };
  },

  methods: {
    LoadOpcState() {
      window.eel.load_slider("/Channel/GeometricAxis/ActProqPos[u1,1]")(
        (result) => {
          this.value_X = result[0];
        }
      );
      window.eel.load_slider("/Channel/GeometricAxis/ActProqPos[u1,2]")(
        (result) => {
          this.value_Y = result[0];
        }
      );
    },
  },

  mounted: function () {
    this.LoadOpcState();
    window.setInterval(() => {
      this.LoadOpcState();
    }, 1000);
  },
};
</script>