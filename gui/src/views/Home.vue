<template>
  <v-container fluid>
    <div class="home">
      <v-row>
        <v-col cols="3">
          <h2>ON / OFF dopravníků</h2>
          <v-divider></v-divider>
          <br />
          <Switches />
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="4">
          <h2>Rychlost dopravníků</h2>
          <v-divider></v-divider>
          <br /><br />
          <Sliders />
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="3">
          <h2>Stav lakovny</h2>
          <v-divider></v-divider>
          <br />
          <Indicators />
        </v-col>
      </v-row>
    </div>
  </v-container>
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

<style scoped>
.home {
  margin-left: 50px;
  margin-right: 50px;
}
</style>