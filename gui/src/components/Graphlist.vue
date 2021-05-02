 <template>
  <v-card class="mx-auto" width="300">
    <v-list rounded="true">
      <v-list-item>
        <v-list-item-title class="title"> Graph choice</v-list-item-title>
      </v-list-item>
      <v-list-item-group v-model="selectedItem" color="primary">
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="handleClick(index)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        title: "Unloading cycle time",
        click() {
          const plotly_payload = {
            promenna: "unloadingCycleTime",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Oven1 Temperature1",
        click() {
          const plotly_payload = {
            promenna: "oven1Temperature1",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Oven2 Temperature1",
        click() {
          const plotly_payload = {
            promenna: "oven2Temperature1",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Oven 2 Temperature2",
        click() {
          const plotly_payload = {
            promenna: "oven2Temperature2",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Oven2 Temperature3",
        click() {
          const plotly_payload = {
            promenna: "oven2Temperature3",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Oven2 Temperature4",
        click() {
          const plotly_payload = {
            promenna: "oven2Temperature4",
            casovani: "Timing",
          };
          this.$store.commit("mutate_plotly_payload", {
            payload: plotly_payload,
          });
          this.$store.dispatch("get_plot");
        },
      },
    ],
  }),
  methods: {
    handleClick(index) {
      this.items[index].click.call(this);
    },
  },
};
</script>