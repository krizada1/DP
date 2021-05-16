<template>
  <v-container fluid>
    <v-row>
      <v-switch v-model="blasterAuto" color="green" disabled>
        <template v-slot:label> blasterAuto </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="Cabine1Online" color="green" disabled>
        <template v-slot:label> Cabine1Online </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="oven1PowerOff" color="green" disabled>
        <template v-slot:label> oven1PowerOff </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="CoolingZone1PowerOn" color="green" disabled>
        <template v-slot:label> CoolingZone1PowerOn </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="Cabine2Online" color="green" disabled>
        <template v-slot:label> Cabine2Online </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="CoolingZone2PowerOn" color="green" disabled>
        <template v-slot:label> CoolingZone2PowerOn </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="oven2PowerOff" color="green" disabled>
        <template v-slot:label> oven2PowerOff </template>
      </v-switch>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      blasterAuto: true,
      Cabine1Online: true,
      oven1PowerOff: true,
      CoolingZone1PowerOn: true,
      Cabine2Online: true,
      CoolingZone2PowerOn: true,
      oven2PowerOff: true,
    };
  },

  methods: {
    load_data() {
      window.eel.nacti_switch(
        "blasterAuto",
        "Cabine1Online",
        "oven1PowerOff",
        "CoolingZone1PowerOn",
        "Cabine2Online",
        "CoolingZone2PowerOn",
        "oven2PowerOff"
      )((result) => {
        this.blasterAuto = result[0];
        this.Cabine1Online = result[1];
        this.oven1PowerOff = !result[2];
        this.CoolingZone1PowerOn = result[3];
        this.Cabine2Online = result[4];
        this.CoolingZone2PowerOn = result[5];
        this.oven2PowerOff = !result[6];
      });
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