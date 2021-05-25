<template>
  <v-container fluid style="margin: 35px; padding: 0px; width: 95%">
    <div class="home">
      <v-row>
        <v-col><Alarmtable /></v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
// @ is an alias to /src
import Alarmtable from "@/components/Alarmtable.vue";

export default {
  name: "Alarm",
  components: {
    Alarmtable,
  },

  data() {
    return {};
  },
};
</script>