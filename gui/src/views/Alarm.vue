<template>
  <div class="home">
    <v-row>
      <v-col><Alarmlist /></v-col>
      <v-col></v-col>
      <v-col></v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import Alarmlist from "@/components/Alarmlist.vue";

export default {
  name: "Alarm",
  components: {
    Alarmlist,
  },

  data() {
    return {};
  },
};
</script>