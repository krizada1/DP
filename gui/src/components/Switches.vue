<template>
  <v-container fluid>
    <v-row justify="center">
      <v-switch v-model="D1" color="green" @click="ChangeSwitch('D1Move', D1)">
        <template v-slot:label>
          D1 Move..<v-progress-circular
            :indeterminate="D1"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="D2" color="green" @click="ChangeSwitch('D2Move', D2)">
        <template v-slot:label>
          D2 Move..<v-progress-circular
            :indeterminate="D2"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="D3" color="green" @click="ChangeSwitch('D3Move', D3)">
        <template v-slot:label>
          D3 Move..<v-progress-circular
            :indeterminate="D3"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="D4" color="green" @click="ChangeSwitch('D4Move', D4)">
        <template v-slot:label>
          D4 Move..<v-progress-circular
            :indeterminate="D4"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="D5" color="green" @click="ChangeSwitch('D5Move', D5)">
        <template v-slot:label>
          D5 Move..<v-progress-circular
            :indeterminate="D5"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="P2" color="green" @click="ChangeSwitch('P2Move', P2)">
        <template v-slot:label>
          P2 Move..<v-progress-circular
            :indeterminate="P2"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch v-model="P3" color="green" @click="ChangeSwitch('P3Move', P3)">
        <template v-slot:label>
          P3 Move..<v-progress-circular
            :indeterminate="P3"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      D1: true,
      D2: true,
      D3: true,
      D4: true,
      D5: true,
      P2: true,
      P3: true,
    };
  },

  methods: {
    load_data() {
      window.eel.nacti_switch(
        "D1Move",
        "D2Move",
        "D3Move",
        "D4Move",
        "D5Move",
        "P2Move",
        "P3Move"
      )((result) => {
        this.D1 = result[0];
        this.D2 = result[1];
        this.D3 = result[2];
        this.D4 = result[3];
        this.D5 = result[4];
        this.P2 = result[5];
        this.P3 = result[6];
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
