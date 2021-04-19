<template>
  <div class="home">
    <v-row>
      <v-col><Graphlist /></v-col>
      <v-col><HelloWorld /></v-col>
      <v-col></v-col>
      <v-col></v-col>
      <Plotly
        v-if="show_data_loaded_plot"
        :data="plotly_data"
        :layout="{ ...layout, height: 550 }"
        class="mt-4"
      ></Plotly>
      <Plotly
        v-if="show_data_loaded_plot"
        :data="plotly_data"
        :layout="{ ...layout, height: 550 }"
        class="mt-4"
      ></Plotly>
      <Plotly
        v-if="show_data_loaded_plot"
        :data="plotly_data"
        :layout="{ ...layout, height: 550 }"
        class="mt-4"
      ></Plotly>
      <Plotly
        v-if="show_data_loaded_plot"
        :data="plotly_data"
        :layout="{ ...layout, height: 550 }"
        class="mt-4"
      ></Plotly>
      <Plotly
        v-if="show_data_loaded_plot"
        :data="plotly_data"
        :layout="{ ...layout, height: 550 }"
        class="mt-4"
      ></Plotly>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Graphlist from "@/components/Graphlist.vue";
import { mapState } from "vuex";

import { Plotly } from "vue-plotly";

export default {
  name: "Graph",
  components: {
    HelloWorld,
    Graphlist,
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
