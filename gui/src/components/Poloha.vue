<template>
  <div class="text-center">
    <v-row justify="center"> X: {{ value_X }} </v-row>
    <br />
    <v-row justify="center"> Y: {{ value_Y }} </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value_X: "nedefinovano",
      value_Y: "nedefinovano",
    };
  },
};
</script>