<template>
  <v-container fluid>
    <div class="home">
      <v-row>
        <v-col>
          <h2>Poloha</h2>
          <v-divider></v-divider>
          <br />
          <br />
          <h2><Poloha /></h2>
        </v-col>
        <v-col>
          <h2>Override - posuv F</h2>
          <v-divider></v-divider>
          <br />
          <Override_F />
        </v-col>
        <v-col>
          <h2>Override - otáčky S</h2>
          <v-divider></v-divider>
          <br />
          <Override_S />
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
      <v-col>
        <Plotly
          v-if="show_data_loaded_plot"
          :data="plotly_data"
          :layout="{ ...layout }"
          class="mt-4"
        >
        </Plotly
      ></v-col>
    </div>
  </v-container>
</template>

<script>
// @ is an alias to /src
import Override_F from "@/components/Override_F.vue";
import Override_S from "@/components/Override_S.vue";
import Poloha from "@/components/Poloha.vue";

import { Plotly } from "vue-plotly";
import { mapState } from "vuex";

export default {
  name: "Home",
  components: {
    Override_F,
    Override_S,
    Plotly,
    Poloha,
  },

  data() {
    return {
      show_data_loaded_plot: true,
      layout: {
        margin: { l: 50, r: 50, b: 0, t: 40, pad: 8 },
        font: {
          family: "roboto",
        },
        autosize: "false",
        width: 1000,
        height: 500,
        xaxis: {
          type: "date",
          tickformat: "%y/%m/%d %H:%M:%S",
          tickmode: "array",
          tickangle: "45",
          visible: true,
          showticklabels: true,
        },

        legend: {
          orientation: "h",
          y: -0.2,
        },
        hovermode: "closest",
      },
      // data: [
      //   {
      //     x: [1, 2, 3, 4],
      //     y: [10, 15, 13, 17],
      //     type: "scatter",
      //   },
      // ],
    };
  },
  computed: {
    ...mapState(["plotly_data"]),
  },
};
</script>


<style scoped>
.home {
  margin-left: 50px;
  margin-right: 50px;
}
</style>