 <template>
  <v-card class="mx-auto" width="300">
    <v-list rounded="true">
      <v-list-item>
        <v-list-item-title class="title"> Interval</v-list-item-title>
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
    selectedItem: 0,

    items: [
      {
        title: "Last minute",
        click() {
          const plotly_payload_numberofrecords = {
            pocet_zaznamu: 12,
          };
          this.$store.commit("mutate_plotly_payload_numberofrecords", {
            payload: plotly_payload_numberofrecords,
          });
          this.$store.dispatch("get_plot");
        },
      },
      {
        title: "Last hour",
        click() {
          const plotly_payload_numberofrecords = {
            pocet_zaznamu: 720,
          };
          this.$store.commit("mutate_plotly_payload_numberofrecords", {
            payload: plotly_payload_numberofrecords,
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