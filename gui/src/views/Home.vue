<template>
  <div class="home">
    <v-row><br /></v-row>
    <v-row><br /></v-row>
    <v-row><br /></v-row>
    <v-row>
      <v-col><h2>ON / OFF dopravníků</h2></v-col>
      <v-col><h2>Rychlost dopravníků</h2></v-col>
      <v-col><h2>Stav lakovny</h2></v-col>
    </v-row>
    <v-row>
      <v-col><v-divider></v-divider><br /><Switches /></v-col>
      <v-col><v-divider></v-divider><br /><br /><br /><Sliders /></v-col>
      <v-col><v-divider></v-divider><br /><Indicators /></v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import Switches from "@/components/Switches.vue";
import Sliders from "@/components/Sliders.vue";
import Indicators from "@/components/Indicators.vue";

export default {
  name: "Home",
  components: {
    Switches,
    Sliders,
    Indicators,
  },
};
</script>
