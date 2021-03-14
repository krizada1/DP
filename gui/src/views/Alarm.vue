<template>
  <v-card
    class="mx-auto"
    width="300"
  >
    <v-list>
      <v-list-item>
            <v-list-item-title>Alarm choice</v-list-item-title>
      </v-list-item>

          <v-list-item
            v-for="([title, icon], i) in helpers"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        

        <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Ovens</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>

        <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Painting booths</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in cruds"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
      
    </v-list>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
        helpers: [
        ['All'],
        ['Sandblasting'],

      ],
      admins: [
        ['Oven1'],
        ['Oven2'],
      ],
      cruds: [
        ['Painting booth 1'],
        ['Painting booth 2'],
      ],
    }),
  }
</script>