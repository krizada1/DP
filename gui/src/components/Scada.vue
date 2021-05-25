<template>
  <v-container fluid>
    <v-row justify="center">
      <v-btn
        v-if="!ctrl"
        @click="ChangeSwitch('control', true)"
        class="ma-2"
        color="red"
        dark
      >
        Scada control not active. You can overtake paintshop control by clicking
        on this button.
        <v-icon dark right> mdi-cancel </v-icon>
      </v-btn>
      <v-alert v-if="ctrl" class="alert" color="green" dark>
        SCADA CONTROL IS ACTIVE! YOU CAN CONTROL PAINTSHOP NOW.
        <v-icon dark right> mdi-checkbox-marked-circle </v-icon>
      </v-alert>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      ctrl: false,
    };
  },

  methods: {
    load_data() {
      window.eel.load_scada("control")((result) => {
        this.ctrl = result[0];
      });
    },

    ChangeSwitch(variable, value) {
      window.eel.set_switch_value(variable, value);
    },
  },

  mounted: function () {
    this.load_data();
    window.setInterval(() => {
      this.load_data();
    }, 5000);
  },
};
</script>

<style scoped>
.alert {
  align-self: flex-start;
  padding: 7px;
}
</style>