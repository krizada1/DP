<template>
  <v-container fluid>
    <v-row justify="center">
      <v-switch
        v-model="D1Move"
        color="green"
        @click="ChangeSwitch('D1Move', D1Move)"
      >
        <template v-slot:label>
          D1 Move..<v-progress-circular
            v-if="Circular.D1Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="D2Move"
        color="green"
        @click="ChangeSwitch('D2Move', D2Move)"
      >
        <template v-slot:label>
          D2 Move..<v-progress-circular
            v-if="Circular.D2Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="D3Move"
        color="green"
        @click="ChangeSwitch('D3Move', D3Move)"
      >
        <template v-slot:label>
          D3 Move..<v-progress-circular
            v-if="Circular.D3Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="D4Move"
        color="green"
        @click="ChangeSwitch('D4Move', D4Move)"
      >
        <template v-slot:label>
          D4 Move..<v-progress-circular
            v-if="Circular.D4Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="D5Move"
        color="green"
        @click="ChangeSwitch('D5Move', D5Move)"
      >
        <template v-slot:label>
          D5 Move..<v-progress-circular
            v-if="Circular.D5Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="P2Move"
        color="green"
        @click="ChangeSwitch('P2Move', P2Move)"
      >
        <template v-slot:label>
          P2 Move..<v-progress-circular
            v-if="Circular.P2Move"
            :indeterminate="true"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-row>
    <v-row justify="center">
      <v-switch
        v-model="P3Move"
        color="green"
        @click="ChangeSwitch('P3Move', P3Move)"
      >
        <template v-slot:label>
          P3 Move..<v-progress-circular
            v-if="Circular.P3Move"
            :indeterminate="true"
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
      D1Move: true,
      D2Move: true,
      D3Move: true,
      D4Move: true,
      D5Move: true,
      P2Move: true,
      P3Move: true,

      OpcArray: {
        D1Move: false,
        D2Move: false,
        D3Move: false,
        D4Move: false,
        D5Move: false,
        P2Move: false,
        P3Move: false,
      },

      TimerVar: "",

      Circular: {
        D1Move: false,
        D2Move: false,
        D3Move: false,
        D4Move: false,
        D5Move: false,
        P2Move: false,
        P3Move: false,
      },
    };
  },

  methods: {
    LoadOpcState() {
      window.eel.load_switch(
        "D1Move",
        "D2Move",
        "D3Move",
        "D4Move",
        "D5Move",
        "P2Move",
        "P3Move"
      )((result) => {
        this.OpcArray.D1Move = result[0];
        this.OpcArray.D2Move = result[1];
        this.OpcArray.D3Move = result[2];
        this.OpcArray.D4Move = result[3];
        this.OpcArray.D5Move = result[4];
        this.OpcArray.P2Move = result[5];
        this.OpcArray.P3Move = result[6];
      });
    },

    UpdateSwitches() {
      this.D1Move = this.OpcArray.D1Move;
      this.D2Move = this.OpcArray.D2Move;
      this.D3Move = this.OpcArray.D3Move;
      this.D4Move = this.OpcArray.D4Move;
      this.D5Move = this.OpcArray.D5Move;
      this.P2Move = this.OpcArray.P2Move;
      this.P3Move = this.OpcArray.P3Move;
    },

    ChangeSwitch(variable, value) {
      if (variable == "D1Move") {
        this.Circular.D1Move = true;
      }
      if (variable == "D2Move") {
        this.Circular.D2Move = true;
      }
      if (variable == "D3Move") {
        this.Circular.D3Move = true;
      }
      if (variable == "D4Move") {
        this.Circular.D4Move = true;
      }
      if (variable == "D5Move") {
        this.Circular.D5Move = true;
      }
      if (variable == "P2Move") {
        this.Circular.P2Move = true;
      }
      if (variable == "P3Move") {
        this.Circular.P3Move = true;
      }
      window.clearTimeout(this.TimerVar);
      window.eel.set_switch_value(variable, value);
      this.TimerVar = window.setTimeout(() => {
        this.UpdateSwitches();
      }, 5000);
      window.setTimeout(() => {
        if (variable == "D1Move") {
          this.Circular.D1Move = false;
        }
        if (variable == "D2Move") {
          this.Circular.D2Move = false;
        }
        if (variable == "D3Move") {
          this.Circular.D3Move = false;
        }
        if (variable == "D4Move") {
          this.Circular.D4Move = false;
        }
        if (variable == "D5Move") {
          this.Circular.D5Move = false;
        }
        if (variable == "P2Move") {
          this.Circular.P2Move = false;
        }
        if (variable == "P3Move") {
          this.Circular.P3Move = false;
        }
      }, 5000);
    },
  },

  mounted: function () {
    this.LoadOpcState();
    window.setInterval(() => {
      this.LoadOpcState();
    }, 1000);
  },

  watch: {
    OpcArray: {
      handler: function () {
        this.UpdateSwitches();
      },
      deep: true,
    },
  },
};
</script>
