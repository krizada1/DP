 <template>
  <v-card class="mx-auto" width="300">
    <v-list rounded="true">
      <v-list-item>
        <v-list-item-title class="title"> Alarm choice</v-list-item-title>
      </v-list-item>
      <v-list-item
        v-for="(item, index) in items"
        :key="index"
        @click="handleClick(index)"
      >
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        title: "All",
        click() {
          console.log("all");
        },
      },
      {
        title: "Sandblaster",
        click() {
          console.log("Sandblaster");
        },
      },
      {
        title: "Oven 1",
        click() {
          console.log("Oven 1");
        },
      },
      {
        title: "Oven 2",
        click() {
          console.log("Oven 2");
        },
      },
      {
        title: "Painting booth 1",
        click() {
          console.log("Painting booth 1");
        },
      },
      {
        title: "Painting booth 2",
        click() {
          console.log("Painting booth 2");
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