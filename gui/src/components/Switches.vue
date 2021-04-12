<template>
  <v-container fluid>
    <v-app>
      <v-switch v-model="D1">
        <template v-slot:label>
          D1 Move..<v-progress-circular
            :indeterminate="D1"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="D2">
        <template v-slot:label>
          D2 Move..<v-progress-circular
            :indeterminate="D2"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="D3">
        <template v-slot:label>
          D3 Move..<v-progress-circular
            :indeterminate="D3"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="D4">
        <template v-slot:label>
          D4 Move..<v-progress-circular
            :indeterminate="D4"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="D5">
        <template v-slot:label>
          D5 Move..<v-progress-circular
            :indeterminate="D5"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="P2">
        <template v-slot:label>
          P2 Move..<v-progress-circular
            :indeterminate="P2"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
      <v-switch v-model="P3">
        <template v-slot:label>
          P3 Move..<v-progress-circular
            :indeterminate="P3"
            :value="0"
            size="20"
            class="ml-2"
          ></v-progress-circular>
        </template>
      </v-switch>
    </v-app>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      D1: true,
      D2: false,
      D3: window.eel.nacti_z_db2("D3Move", 1),
      D4: window.eel.nacti_z_db2("D4Move", 1),
      D5: window.eel.nacti_z_db2("D5Move", 1),
      P2: window.eel.nacti_z_db2("P2Move", 1),
      P3: window.eel.nacti_z_db2("P3Move", 1),
    };
  },

  methods: {
    load_data() {
      this.D1 = window.eel.nacti_z_db2("D1Move", 1);
    },
  },

  mounted: function () {
    this.load_data();
  },
};
</script>