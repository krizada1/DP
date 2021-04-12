<template>
  <v-container fluid>
      <v-app>
        <v-row>
       
            <v-slider
            v-model="D1Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="D1 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
        <v-row>
            <v-slider
            v-model="D2Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="D2 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
         <v-row>
            <v-slider
            v-model="D3Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="D3 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
         <v-row>
            <v-slider
            v-model="D4Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="D4 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
         <v-row>
            <v-slider
            v-model="D5Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="D5 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
         <v-row>
            <v-slider
            v-model="P2Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="P2 Speed"
            persistent-hint
            ></v-slider>
        </v-row>
         <v-row>
            <v-slider
            v-model="P3Speed"
            thumb-label="always"
            step="10"
            min="4000"
            max="5000"
            hint="P3 Speed"
            persistent-hint
            ></v-slider>
        </v-row>

      </v-app>
  </v-container>
</template>

<script>
export default {
     data () {
      return {
        D1Speed: 4000,
        D2Speed: 4150,
        D3Speed: 4300,
        D4Speed: 4500,
        D5Speed: 4650,
        P2Speed: 4800,
        P3Speed: 5000,
      }
    },
}
</script>
