<template>
  <v-container fluid>
    <v-row>
      <v-switch v-model="blasterAuto" color="green" disabled>
        <template v-slot:label> Blaster </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="Cabine1Online" color="green" disabled>
        <template v-slot:label> Painting booth 1 </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="oven1PowerOff" color="green" disabled>
        <template v-slot:label> Oven 1 </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="CoolingZone1PowerOn" color="green" disabled>
        <template v-slot:label> Cooling Zone 1 </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="Cabine2Online" color="green" disabled>
        <template v-slot:label> Painting booth 2 </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="CoolingZone2PowerOn" color="green" disabled>
        <template v-slot:label> Cooling Zone 2 </template>
      </v-switch>
    </v-row>
    <v-row>
      <v-switch v-model="oven2PowerOff" color="green" disabled>
        <template v-slot:label> Oven 2 </template>
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
    LoadOpcState() {
      window.eel.load_switch(
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
    this.LoadOpcState();
    window.setInterval(() => {
      this.LoadOpcState();
    }, 1000);
  },
};
</script>