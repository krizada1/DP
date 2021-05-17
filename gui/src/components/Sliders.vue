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
        @end="ChangeSlider('D1Speed', D1Speed)"
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
        @end="ChangeSlider('D2Speed', D2Speed)"
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
        @end="ChangeSlider('D3Speed', D3Speed)"
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
        @end="ChangeSlider('D4Speed', D4Speed)"
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
        @end="ChangeSlider('D5Speed', D5Speed)"
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
        @end="ChangeSlider('P2Speed', P2Speed)"
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
        @end="ChangeSlider('P3Speed', P3Speed)"
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
      OpcArray: {
        a: false,
        b: false,
        c: false,
        d: false,
        e: false,
        f: false,
        g: false,
      },
      TimerVar: "",
    };
  },

  methods: {
    LoadOpcState() {
      window.eel.nacti_slider(
        "D1Speed",
        "D2Speed",
        "D3Speed",
        "D4Speed",
        "D5Speed",
        "P2Speed",
        "P3Speed"
      )((result) => {
        this.OpcArray.a = result[0];
        this.OpcArray.b = result[1];
        this.OpcArray.c = result[2];
        this.OpcArray.d = result[3];
        this.OpcArray.e = result[4];
        this.OpcArray.f = result[5];
        this.OpcArray.g = result[6];
      });
    },

    UpdateSliders() {
      this.D1Speed = this.OpcArray.a;
      this.D2Speed = this.OpcArray.b;
      this.D3Speed = this.OpcArray.c;
      this.D4Speed = this.OpcArray.d;
      this.D5Speed = this.OpcArray.e;
      this.P2Speed = this.OpcArray.f;
      this.P3Speed = this.OpcArray.g;
    },

    ChangeSlider(variable, value) {
      window.clearTimeout(this.TimerVar);
      window.eel.set_slider_value(variable, value);
      this.TimerVar = window.setTimeout(() => {
        this.UpdateSwitches();
      }, 4000);
    },
  },

  mounted: function () {
    this.LoadOpcState();
    window.setInterval(() => {
      this.LoadOpcState();
    }, 1000);
  },

  watch: {
    OpcArray: {
      handler: function () {
        this.UpdateSliders();
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.slider {
  height: 66px;
}
</style>