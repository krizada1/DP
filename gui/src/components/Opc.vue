<template>
  <v-container fluid>
    <v-row justify="center">
      <v-alert v-if="!opc" class="alert" color="red" dark>
        OPC SERVER UNAVAILABLE, CONTROL OF PAINTSHOP IS NOT POSSIBLE!
      </v-alert>
      <v-alert v-if="opc" class="alert" color="green" dark>
        OPC SERVER CONNECTED, CONTROL OF PAINTSHOP IS POSSIBLE!
      </v-alert>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      opc: false,
    };
  },

  methods: {
    connect_opc() {
      window.eel.connect_opc()((result) => {
        this.opc = result;
      });
    },
  },

  mounted: function () {
    this.connect_opc();
    window.setInterval(() => {
      this.connect_opc();
    }, 5000);
  },
};
</script>

<style scoped>
.alert {
  padding: 7px;
}
</style>