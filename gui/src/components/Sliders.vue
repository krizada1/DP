<template>
  <v-container fluid>
    <v-row>
      <v-slider
        class="slider"
        v-model="D1Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="D1 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="D2Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="D2 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="D3Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="D3 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="D4Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="D4 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="D5Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="D5 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="P2Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="P2 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
    <v-row>
      <v-slider
        class="slider"
        v-model="P3Speed"
        thumb-label="always"
        step="10"
        min="0"
        max="7000"
        hint="P3 Speed"
        persistent-hint
      ></v-slider>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      D1Speed: 6000,
      D2Speed: 6000,
      D3Speed: 6000,
      D4Speed: 6000,
      D5Speed: 6000,
      P2Speed: 6000,
      P3Speed: 6000,
    };
  },

  methods: {
    load_data() {
      window.eel.nacti_slider(
        "D1Speed",
        "D2Speed",
        "D3Speed",
        "D4Speed",
        "D5Speed",
        "P2Speed",
        "P3Speed",
        1
      )((result) => {
        this.D1Speed = result[0];
        this.D2Speed = result[1];
        this.D3Speed = result[2];
        this.D4Speed = result[3];
        this.D5Speed = result[4];
        this.P2Speed = result[5];
        this.P3Speed = result[6];
      });
    },
  },

  mounted: function () {
    this.load_data();
  },
};
</script>

<style scoped>
.slider {
  height: 66px;
}
</style>