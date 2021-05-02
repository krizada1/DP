<template>
  <v-container fluid style="margin: 35px; padding: 0px; width: 100%">
    <div class="home">
      <v-row>
        <v-col cols="2"
          ><v-row><Graphlist /></v-row>
          <v-row><p></p></v-row>
          <v-row><Timelist /></v-row>
        </v-col>
        <v-col>
          <Plotly
            v-if="show_data_loaded_plot"
            :data="plotly_data"
            :layout="{ ...layout }"
            class="mt-4"
          >
          </Plotly>
          <p>
            {{ $store.state.plotly_payload.promenna }}
          </p>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
// @ is an alias to /src
import Graphlist from "@/components/Graphlist.vue";
import Timelist from "@/components/Timelist.vue";
import { mapState } from "vuex";

import { Plotly } from "vue-plotly";

export default {
  name: "Graph",
  components: {
    Graphlist,
    Timelist,
    Plotly,
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
