  <template>
  <v-card>
    <v-card-title class="v-card-title">
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="You can use this as a filter"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="table_data.table"
      :items-per-page="5"
      :search="search"
      class="table"
      ><template
        v-for="header in headers.filter((header) =>
          header.hasOwnProperty('formatter')
        )"
        v-slot:[`item.${header.value}`]="{ value }"
      >
        {{ header.formatter(value) }}
      </template></v-data-table
    >
  </v-card>
</template>

<script>
import moment from "moment";
import { mapState } from "vuex";

export default {
  data: function () {
    return {
      dateFormat: "YYYY-MM-DD HH:mm:ss",
      search: "",
      headers: [
        {
          text: "Location",
          value: "Location",
          align: "center",
        },
        {
          text: "Start time",
          value: "Start time",
          align: "center",
          formatter: (x) => (x ? moment(x).format(this.dateFormat) : null),
        },
        {
          text: "Finish time",
          value: "Finish time",
          align: "center",
          formatter: (x) => (x ? moment(x).format(this.dateFormat) : null),
        },
        {
          text: "Duration [s]",
          value: "Duration",
          align: "center",
        },
      ],
    };
  },

  mounted() {
    this.$store.dispatch("get_table");
  },

  computed: {
    ...mapState(["table_data"]),
  },
};
</script>

