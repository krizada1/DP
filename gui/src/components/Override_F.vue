<template>
  <div class="text-center">
    <v-progress-circular
      :rotate="180"
      :size="100"
      :width="15"
      :value="(value / 120) * 100"
      color="teal"
    >
      {{ value }} %
    </v-progress-circular>
  </div>
</template>

<script>
export default {
  data() {
    return {
      interval: {},
      value: 50,
    };
  },

  methods: {
    LoadOpcState() {
      window.eel.load_slider("/Channel/State/feedRatelpoOvr")((result) => {
        this.value = result[0];
      });
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

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>